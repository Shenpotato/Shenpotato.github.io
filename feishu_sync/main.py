import os
import re
import time
import json
from datetime import datetime
from dotenv import load_dotenv

from feishu_client import FeishuClient
from markdown_converter import MarkdownConverter
from post_manager import PostManager

load_dotenv()


class FeishuSyncAgent:
    def __init__(self):
        self.feishu_client = FeishuClient()

        posts_dir = os.path.abspath(os.getenv('POSTS_DIR', '../_posts'))
        img_dir = os.path.abspath(os.getenv('IMG_DIR', '../img/in-post'))

        # 自动检测环境
        # 常见的 CI/服务器环境变量
        ci_env_vars = ['CI', 'GITHUB_ACTIONS',
                       'NETLIFY', 'VERCEL', 'RENDER', 'PAGES']
        is_ci_env = any(os.getenv(var) for var in ci_env_vars)

        # 优先使用环境变量配置，如果没有则根据环境自动判断
        env_use_relative = os.getenv('USE_RELATIVE_IMAGE_PATH')
        if env_use_relative is not None:
            use_relative_path = env_use_relative.lower() == 'true'
        else:
            # CI/服务器环境使用绝对路径，本地环境使用相对路径
            use_relative_path = not is_ci_env

        print(
            f'Using {"relative" if use_relative_path else "absolute"} image paths')

        self.post_manager = PostManager(posts_dir)
        self.markdown_converter = MarkdownConverter(
            img_dir, posts_dir, use_relative_path)
        self.markdown_converter.set_image_download_callback(
            self._download_image)
        self.markdown_converter.set_board_download_callback(
            self._download_board)

        self.sync_interval = int(os.getenv('SYNC_INTERVAL_MINUTES', 60))
        self.root_folder_token = os.getenv('FEISHU_ROOT_FOLDER_TOKEN')
        # 忽略示例值
        if self.root_folder_token and 'optional' in self.root_folder_token.lower():
            self.root_folder_token = None

        self.state_file = os.path.join(
            os.path.dirname(__file__), 'sync_state.json')
        self.last_sync_times = self._load_sync_state()

    def _load_sync_state(self) -> dict:
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}

    def _save_sync_state(self):
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(self.last_sync_times, f, ensure_ascii=False, indent=2)

    def _extract_token_from_url(self, url: str) -> tuple:
        wiki_match = re.search(r'wiki/([a-zA-Z0-9]+)', url)
        if wiki_match:
            return ('wiki', wiki_match.group(1))

        docx_match = re.search(r'docx/([a-zA-Z0-9]+)', url)
        if docx_match:
            return ('docx', docx_match.group(1))

        doc_match = re.search(r'docs/([a-zA-Z0-9]+)', url)
        if doc_match:
            return ('doc', doc_match.group(1))

        folder_match = re.search(r'folder/([a-zA-Z0-9]+)', url)
        if folder_match:
            return ('folder', folder_match.group(1))

        return (None, None)

    def _download_image(self, token: str) -> bytes:
        return self.feishu_client.download_media(token)

    def _download_board(self, token: str) -> bytes:
        return self.feishu_client.download_board_as_image(token)

    def _extract_categories_and_tags(self, doc_info: dict) -> tuple:
        categories = []
        tags = []

        title = doc_info.get('title', '')
        if title:
            if 'AI' in title or 'ai' in title or '机器学习' in title:
                categories.append('ai')
            if '算法' in title:
                categories.append('algorithm')
            if '后端' in title or 'Backend' in title:
                categories.append('backend')
            if '前端' in title or 'Frontend' in title:
                categories.append('frontend')
            if '网络' in title or 'Network' in title:
                categories.append('network')
            if '编程' in title or '语言' in title:
                categories.append('program_language')
            if '工具' in title or 'Utils' in title:
                categories.append('utils')
            if 'Web3' in title or 'web3' in title:
                categories.append('web3')
            if '个人' in title or 'Personal' in title or '思考' in title:
                categories.append('personal')

        return categories, tags

    def _convert_docx_document(self, document_id: str, doc_info: dict):
        document = doc_info.get('document', {})
        title = document.get('title', doc_info.get('title', 'Untitled'))
        create_time = document.get('create_time', doc_info.get('create_time'))

        if create_time:
            doc_date = datetime.fromtimestamp(int(create_time) / 1000)
        else:
            doc_date = datetime.now()

        print(f'Processing document: {title} ({document_id})')

        # 先获取分类和翻译标题
        categories, tags = self._extract_categories_and_tags(doc_info)
        translated_title = self.post_manager.translate_title(title)

        # 先获取 blocks，但不转换
        blocks_response = self.feishu_client.get_document_blocks(document_id)
        blocks = blocks_response.get('data', {}).get('items', [])

        # 先确定文章会保存到哪个目录，用于计算相对路径
        final_categories = self.post_manager.get_category_from_content(
            title, '', categories)
        category_dir = self.post_manager.get_category_dir(final_categories)

        # 使用翻译后的标题设置图片文件夹，并传入最终的文章目录
        self.markdown_converter.set_document_context(
            title, doc_date, translated_title)
        # 更新 markdown_converter 的 posts_dir 为最终的分类目录，这样相对路径计算正确
        self.markdown_converter.posts_dir = category_dir

        markdown_content = self.markdown_converter.convert_blocks_to_markdown(
            blocks)

        try:
            filepath = self.post_manager.save_post(
                title=title,
                content=markdown_content,
                tags=tags,
                categories=categories,
                date=doc_date,
                published=False,
                overwrite=True
            )
            print(f'Successfully saved post: {filepath}')
            return True
        except Exception as e:
            print(f'Failed to save post: {e}')
            return False

    def sync_single_document(self, url_or_token: str):
        doc_type, token = self._extract_token_from_url(url_or_token)

        if not token:
            token = url_or_token

        try:
            if doc_type == 'wiki' or (not doc_type and token):
                print(f'Trying to process as wiki node: {token}')
                wiki_node_response = self.feishu_client.get_wiki_node(
                    token, obj_type='wiki')
                wiki_node = wiki_node_response.get('data', {}).get('node', {})
                obj_type = wiki_node.get('obj_type')
                obj_token = wiki_node.get('obj_token')
                title = wiki_node.get('title', 'Untitled')
                obj_create_time = wiki_node.get('obj_create_time')

                if obj_type == 'docx' and obj_token:
                    print(f'Wiki node points to docx document: {obj_token}')
                    doc_info_response = self.feishu_client.get_document_info(
                        obj_token)
                    doc_info = doc_info_response.get('data', {})
                    doc_info['title'] = title
                    if obj_create_time:
                        doc_info['create_time'] = str(
                            int(obj_create_time) * 1000)

                    if self._convert_docx_document(obj_token, doc_info):
                        self.last_sync_times[token] = int(time.time() * 1000)
                        self._save_sync_state()
                else:
                    print(f'Unsupported wiki node type: {obj_type}')

            elif doc_type == 'docx' or (not doc_type and token):
                print(f'Trying to process as docx document: {token}')
                doc_info_response = self.feishu_client.get_document_info(token)
                doc_info = doc_info_response.get('data', {})

                if self._convert_docx_document(token, doc_info):
                    self.last_sync_times[token] = int(time.time() * 1000)
                    self._save_sync_state()

            else:
                print(f'Unsupported document type: {doc_type}')

        except Exception as e:
            print(f'Failed to sync document: {e}')
            import traceback
            traceback.print_exc()

    def _sync_folder(self, folder_token: str):
        print(f'Scanning folder: {folder_token}')
        files_response = self.feishu_client.list_files_in_folder(folder_token)
        files = files_response.get('data', {}).get('files', [])

        if not files:
            print(f'  No items found in folder.')

        for file in files:
            file_token = file.get('token')
            file_type = file.get('type')
            file_name = file.get('name')
            edited_time = int(file.get('edited_time', 0))

            print(
                f'Found item: {file_name}, type={file_type}, token={file_token}')

            # 如果是 shortcut，尝试获取实际文件的 token
            actual_token = file_token
            if file_type == 'shortcut':
                # shortcut_info 里有 target_token
                if 'shortcut_info' in file and isinstance(file.get('shortcut_info'), dict):
                    shortcut_info = file.get('shortcut_info', {})
                    if 'target_token' in shortcut_info:
                        actual_token = shortcut_info.get('target_token')
                        print(
                            f'  Found target_token in shortcut: {actual_token}')

            if file_type == 'folder':
                self._sync_folder(file_token)
            elif file_type == 'docx' or file_type == 'shortcut':
                last_sync = self.last_sync_times.get(actual_token, 0)
                # 如果 edited_time 是 0，或者文件确实更新了，就同步
                if edited_time == 0 or edited_time > last_sync:
                    try:
                        print(
                            f'Processing document: {file_name} (type={file_type}, actual_token={actual_token})')
                        doc_info_response = self.feishu_client.get_document_info(
                            actual_token)
                        doc_info = doc_info_response.get('data', {})

                        if self._convert_docx_document(actual_token, doc_info):
                            self.last_sync_times[actual_token] = int(
                                time.time() * 1000)
                            # 也保存 shortcut 的 token，避免重复
                            if file_type == 'shortcut' and actual_token != file_token:
                                self.last_sync_times[file_token] = int(
                                    time.time() * 1000)
                    except Exception as e:
                        print(f'Failed to process document {file_name}: {e}')
                else:
                    print(f'Skipping unchanged document: {file_name}')

    def run_once(self):
        print(
            f'Starting sync at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

        try:
            if self.root_folder_token:
                self._sync_folder(self.root_folder_token)
            else:
                root_folder = self.feishu_client.get_root_folder()
                root_token = root_folder.get('data', {}).get('token')
                if root_token:
                    self._sync_folder(root_token)

            self._save_sync_state()
            print('Sync completed successfully')
        except Exception as e:
            print(f'Sync failed: {e}')
            import traceback
            traceback.print_exc()

    def run_loop(self):
        print(
            f'Starting agent loop. Sync interval: {self.sync_interval} minutes')

        while True:
            self.run_once()

            print(f'Waiting {self.sync_interval} minutes before next sync...')
            time.sleep(self.sync_interval * 60)


def main():
    import sys

    agent = FeishuSyncAgent()

    if len(sys.argv) > 1:
        if sys.argv[1] == '--once':
            agent.run_once()
        elif sys.argv[1] == '--doc' and len(sys.argv) > 2:
            agent.sync_single_document(sys.argv[2])
        else:
            print('Usage:')
            print('  python main.py --once          - Run sync once')
            print(
                '  python main.py --doc <url>     - Sync single document by URL or token')
            print('  python main.py                  - Run agent loop')
    else:
        agent.run_loop()


if __name__ == '__main__':
    main()
