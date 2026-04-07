import os
import re
import hashlib
from datetime import datetime
from typing import List, Dict, Any, Optional, Callable


class MarkdownConverter:
    def __init__(self, img_base_dir: str, posts_dir: Optional[str] = None, use_relative_path: bool = False):
        self.img_base_dir = img_base_dir
        self.posts_dir = posts_dir
        self.use_relative_path = use_relative_path
        self.current_img_dir = None
        self.image_map = {}
        self.image_download_callback: Optional[Callable[[str], bytes]] = None
        self.board_download_callback: Optional[Callable[[str], bytes]] = None
    
    def set_image_download_callback(self, callback: Callable[[str], bytes]):
        self.image_download_callback = callback
    
    def set_board_download_callback(self, callback: Callable[[str], bytes]):
        self.board_download_callback = callback
    
    def set_document_context(self, doc_title: str, doc_date: datetime, translated_title: Optional[str] = None):
        date_str = doc_date.strftime('%Y%m%d')
        # 使用翻译后的标题作为图片文件夹名称（如果有）
        title_for_folder = translated_title if translated_title else doc_title
        safe_title = re.sub(r'[^\w\-_\. ]', '', title_for_folder)
        safe_title = safe_title.replace(' ', '-')
        self.current_img_dir = os.path.join(self.img_base_dir, f'{date_str}-{safe_title}')
        os.makedirs(self.current_img_dir, exist_ok=True)
    
    def _save_image(self, image_data: bytes, image_ext: str = 'png') -> str:
        if not self.current_img_dir:
            raise ValueError('Document context not set. Call set_document_context first.')
        
        img_hash = hashlib.md5(image_data).hexdigest()[:12]
        img_filename = f'image-{img_hash}.{image_ext}'
        img_path = os.path.join(self.current_img_dir, img_filename)
        
        with open(img_path, 'wb') as f:
            f.write(image_data)
        
        # 生成两种路径
        # 1. 绝对路径（用于 Jekyll 网站）
        absolute_path = os.path.relpath(img_path, start=os.path.dirname(os.path.dirname(self.img_base_dir)))
        absolute_path = absolute_path.replace(os.path.sep, '/')
        
        # 2. 相对路径（用于本地预览）
        if self.posts_dir:
            relative_path = os.path.relpath(img_path, start=self.posts_dir)
            relative_path = relative_path.replace(os.path.sep, '/')
        else:
            relative_path = absolute_path
        
        # 默认返回相对路径（方便本地预览）
        return relative_path
    
    def _get_block_type_name(self, block_type):
        block_type_map = {
            1: 'page',
            2: 'paragraph',
            3: 'heading1',
            4: 'heading2',
            5: 'heading3',
            6: 'heading4',
            7: 'heading5',
            8: 'heading6',
            9: 'heading7',
            10: 'heading8',
            11: 'heading9',
            12: 'bullet_list',
            13: 'numbered_list',
            14: 'code',
            15: 'quote',
            16: 'todo',
            17: 'todo_list',
            18: 'undefined',
            19: 'file',
            20: 'divider',
            21: 'table',
            22: 'table_cell',
            23: 'view',
            24: 'sheet',
            25: 'bitable',
            26: 'mindnote',
            27: 'image',
            28: 'diagram',
            29: 'grid',
            30: 'grid_column',
            31: 'callout',
            32: 'horizontal_rule',
            33: 'isv',
            34: 'quote_container',
            35: 'todo',
            36: 'todo_list',
            37: 'horizontal_rule',
            38: 'callout',
            39: 'isv',
            40: 'undefined',
            41: 'undefined',
            42: 'undefined',
            43: 'board',
        }
        if isinstance(block_type, str):
            return block_type
        return block_type_map.get(block_type, str(block_type))
    
    def _download_and_register_image(self, token: str, image_ext: str = 'png') -> Optional[str]:
        if token in self.image_map:
            return self.image_map[token]
        
        if not self.image_download_callback:
            return None
        
        try:
            image_data = self.image_download_callback(token)
            if image_data:
                return self.register_image(token, image_data, image_ext)
        except Exception as e:
            print(f'Failed to download image {token}: {e}')
        
        return None
    
    def _download_and_register_board(self, token: str, image_ext: str = 'png') -> Optional[str]:
        if token in self.image_map:
            return self.image_map[token]
        
        if not self.board_download_callback:
            return None
        
        try:
            image_data = self.board_download_callback(token)
            if image_data:
                return self.register_image(token, image_data, image_ext)
        except Exception as e:
            print(f'Failed to download board {token}: {e}')
        
        return None
    
    def _convert_block_to_markdown(self, block: Dict[str, Any]) -> str:
        block_type = block.get('block_type')
        block_type_name = self._get_block_type_name(block_type)
        elements = []
        
        if block_type_name in ['paragraph', 2]:
            text_block = block.get('paragraph', block.get('text', {}))
            elements = text_block.get('elements', [])
            text = self._convert_elements_to_text(elements)
            return f'{text}\n\n'
        
        elif block_type_name in ['heading1', 3]:
            heading = block.get('heading1', {})
            elements = heading.get('elements', [])
            text = self._convert_elements_to_text(elements)
            return f'# {text}\n\n'
        
        elif block_type_name in ['heading2', 4]:
            heading = block.get('heading2', {})
            elements = heading.get('elements', [])
            text = self._convert_elements_to_text(elements)
            return f'## {text}\n\n'
        
        elif block_type_name in ['heading3', 5]:
            heading = block.get('heading3', {})
            elements = heading.get('elements', [])
            text = self._convert_elements_to_text(elements)
            return f'### {text}\n\n'
        
        elif block_type_name in ['bullet', 'bullet_list', 12]:
            bullet = block.get('bullet', block.get('bullet_list', {}))
            elements = bullet.get('elements', [])
            text = self._convert_elements_to_text(elements)
            return f'- {text}\n'
        
        elif block_type_name in ['ordered', 'numbered_list', 13]:
            ordered = block.get('ordered', block.get('numbered_list', {}))
            elements = ordered.get('elements', [])
            text = self._convert_elements_to_text(elements)
            num = ordered.get('number', ordered.get('sequence', 1))
            return f'{num}. {text}\n'
        
        elif block_type_name in ['code', 14]:
            code = block.get('code', {})
            language_code = code.get('style', {}).get('language', 0)
            language_map = {
                0: '',
                1: 'plaintext',
                2: 'abap',
                3: 'actionscript',
                4: 'apache',
                5: 'apex',
                6: 'assembly',
                7: 'bash',
                8: 'csharp',
                9: 'cpp',
                10: 'c',
                11: 'clojure',
                12: 'cobol',
                13: 'css',
                14: 'coffee',
                15: 'd',
                16: 'dart',
                17: 'delphi',
                18: 'django',
                19: 'dockerfile',
                20: 'erlang',
                21: 'fortran',
                22: 'foxpro',
                23: 'go',
                24: 'groovy',
                25: 'html',
                26: 'htmlbars',
                27: 'http',
                28: 'java',
                29: 'json',
                30: 'julia',
                31: 'kotlin',
                32: 'latex',
                33: 'less',
                34: 'lisp',
                35: 'livescript',
                36: 'lua',
                37: 'makefile',
                38: 'markdown',
                39: 'matlab',
                40: 'nginx',
                41: 'objectivec',
                42: 'pascal',
                43: 'perl',
                44: 'php',
                45: 'powershell',
                46: 'processing',
                47: 'python',
                48: 'r',
                49: 'ruby',
                50: 'rust',
                51: 'sass',
                52: 'scala',
                53: 'scheme',
                54: 'shell',
                55: 'sql',
                56: 'swift',
                57: 'tcl',
                58: 'tex',
                59: 'typescript',
                60: 'vbscript',
                61: 'verilog',
                62: 'vhdl',
                63: 'xml',
                64: 'yaml'
            }
            language = language_map.get(language_code, '')
            content = code.get('elements', [])
            text = self._convert_elements_to_text(content)
            return f'```{language}\n{text}\n```\n\n'
        
        elif block_type_name in ['quote', 15]:
            quote = block.get('quote', {})
            elements = quote.get('elements', [])
            text = self._convert_elements_to_text(elements)
            quoted_lines = [f'> {line}' for line in text.split('\n')]
            return '\n'.join(quoted_lines) + '\n\n'
        
        elif block_type_name in ['image', 18]:
            image = block.get('image', {})
            token = image.get('token', '')
            if token:
                img_url = self._download_and_register_image(token)
                if img_url:
                    return f'![Image]({img_url})\n\n'
        
        elif block_type_name in ['divider', 'horizontal_rule', 20, 32, 37]:
            return '---\n\n'
        
        elif block_type_name in ['board', 43]:
            board = block.get('board', {})
            token = board.get('token', '')
            if token:
                img_url = self._download_and_register_board(token, 'png')
                if img_url:
                    return f'![Board]({img_url})\n\n'
        
        return ''
    
    def _convert_elements_to_text(self, elements: List[Dict[str, Any]]) -> str:
        result = ''
        for elem in elements:
            if 'text_run' in elem:
                text_run = elem.get('text_run', {})
                content = text_run.get('content', '')
                text_element_style = text_run.get('text_element_style', {})
                
                if text_element_style.get('bold'):
                    content = f'**{content}**'
                if text_element_style.get('italic'):
                    content = f'*{content}*'
                if text_element_style.get('underline'):
                    content = f'__{content}__'
                if text_element_style.get('strikethrough'):
                    content = f'~~{content}~~'
                if text_element_style.get('inline_code'):
                    content = f'`{content}`'
                
                result += content
            elif 'link' in elem:
                link = elem.get('link', {})
                url = link.get('url', '')
                text = link.get('text', url)
                result += f'[{text}]({url})'
        
        return result
    
    def convert_blocks_to_markdown(self, blocks: List[Dict[str, Any]]) -> str:
        markdown = ''
        for block in blocks:
            markdown += self._convert_block_to_markdown(block)
        return markdown.strip()
    
    def register_image(self, token: str, image_data: bytes, image_ext: str = 'png'):
        img_path = self._save_image(image_data, image_ext)
        self.image_map[token] = img_path
        return img_path
