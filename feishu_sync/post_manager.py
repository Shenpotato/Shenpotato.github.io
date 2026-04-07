import os
import re
from datetime import datetime
from typing import Optional, List, Dict, Tuple


class PostManager:
    def __init__(self, posts_dir: str):
        self.posts_dir = posts_dir
        self._ensure_posts_dir()
        
        # 常见中文标题到英文的映射
        self.title_translation_map = {
            '拥塞控制算法': 'Congestion-Control',
            '博客模版': 'Blog-Template',
            'QUIC介绍': 'QUIC-Introduction',
            'Rust': 'Rust',
        }
        
        # 常见的分类关键词映射
        self.category_keywords = {
            'network': ['网络', '拥塞控制', 'TCP', 'UDP', 'QUIC', 'RDMA'],
            'algorithm': ['算法', '排序', '树'],
            'ai': ['AI', '人工智能', '机器学习', 'LLM', '深度学习'],
            'backend': ['后端', 'Spring', 'Redis', 'GraphQL'],
            'frontend': ['前端', 'Vue', 'React'],
            'program_language': ['Rust', 'Java', 'Python', 'Go', 'C++'],
            'web3': ['Web3', '区块链'],
            'utils': ['工具', 'Docker', 'Git', 'Linux'],
            'personal': ['个人', '随笔', '阅读'],
        }
    
    def _ensure_posts_dir(self):
        if not os.path.exists(self.posts_dir):
            os.makedirs(self.posts_dir)
    
    def translate_title(self, title: str) -> str:
        """
        将中文标题翻译成英文（用于文件名）
        优先使用映射表，没有匹配则返回原标题
        """
        # 先尝试完全匹配
        if title in self.title_translation_map:
            return self.title_translation_map[title]
        
        # 如果已经是英文，直接返回
        if re.match(r'^[a-zA-Z0-9\s\-]+$', title):
            return title
        
        # 没有匹配，返回原标题
        return title
    
    def get_category_from_content(
        self, 
        title: str, 
        content: str, 
        categories: Optional[List[str]] = None
    ) -> List[str]:
        """
        根据标题、内容和已有 categories 确定分类
        """
        # 如果已有 categories，直接使用
        if categories:
            return categories if isinstance(categories, list) else [categories]
        
        # 根据标题关键词判断
        for category, keywords in self.category_keywords.items():
            for keyword in keywords:
                if keyword.lower() in title.lower():
                    return [category]
        
        # 根据内容关键词判断
        for category, keywords in self.category_keywords.items():
            for keyword in keywords:
                if keyword.lower() in content.lower():
                    return [category]
        
        # 默认没有分类
        return []
    
    def _slugify(self, text: str) -> str:
        text = re.sub(r'[^\w\s-]', '', text.lower())
        text = re.sub(r'[-\s]+', '-', text)
        return text.strip('-')
    
    def _get_post_filename(self, title: str, date: datetime) -> str:
        date_str = date.strftime('%Y-%m-%d')
        translated_title = self.translate_title(title)
        slug = self._slugify(translated_title)
        return f'{date_str}-{slug}.md'
    
    def get_category_dir(self, categories: Optional[List[str]] = None) -> str:
        if not categories:
            return self.posts_dir
        
        category_path = self.posts_dir
        for category in categories:
            category_path = os.path.join(category_path, category.lower().replace(' ', '-'))
        
        os.makedirs(category_path, exist_ok=True)
        return category_path
    
    def _parse_frontmatter_from_content(self, content: str) -> Tuple[Dict, str]:
        """
        解析内容中的 frontmatter，支持标准的 --- 包裹格式和文档开头的 key: value 格式
        返回 (frontmatter_dict, remaining_content)
        """
        content = content.strip()
        frontmatter = {}
        
        # 先检查标准的 --- 包裹格式
        if content.startswith('---'):
            end_index = content.find('---', 3)
            if end_index != -1:
                frontmatter_str = content[3:end_index].strip()
                lines = frontmatter_str.split('\n')
                for line in lines:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        key = key.strip()
                        value = value.strip()
                        if key in ['tags', 'categories']:
                            if value.startswith('[') and value.endswith(']'):
                                value = [v.strip() for v in value[1:-1].split(',')]
                        frontmatter[key] = value
                remaining_content = content[end_index + 3:].strip()
                return frontmatter, remaining_content
        
        # 检查文档开头是否有非标准的 frontmatter（key: value 格式）
        lines = content.split('\n')
        frontmatter_lines = []
        i = 0
        
        # 常见的 frontmatter keys
        common_keys = ['layout', 'title', 'author', 'catalog', 'published', 'tags', 'categories']
        
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                # 空行，继续
                i += 1
                continue
            if ':' in line:
                key = line.split(':', 1)[0].strip().lower()
                if key in common_keys or any(k in key.lower() for k in common_keys):
                    # 看起来像是 frontmatter
                    frontmatter_lines.append(lines[i])
                    i += 1
                else:
                    # 不像是 frontmatter key，停止
                    break
            else:
                # 没有冒号，可能是 tags/categories 的列表项或者内容
                if frontmatter_lines:
                    # 检查是否是列表项（以 - 开头）
                    if line.startswith('-'):
                        frontmatter_lines.append(lines[i])
                        i += 1
                    else:
                        break
                else:
                    break
        
        if frontmatter_lines:
            # 解析收集到的 frontmatter
            current_key = None
            current_value = None
            for line in frontmatter_lines:
                stripped_line = line.strip()
                if ':' in stripped_line:
                    if current_key:
                        if isinstance(current_value, list):
                            frontmatter[current_key] = current_value
                        else:
                            frontmatter[current_key] = current_value.strip() if current_value else ''
                    key, value = stripped_line.split(':', 1)
                    current_key = key.strip()
                    current_value = value.strip()
                elif stripped_line.startswith('-') and current_key in ['tags', 'categories']:
                    # 列表项
                    if not current_value:
                        current_value = []
                    if isinstance(current_value, str):
                        current_value = [current_value]
                    current_value.append(stripped_line[1:].strip())
                else:
                    # 继续追加到当前值（仅当不是列表时）
                    if current_value and not isinstance(current_value, list):
                        current_value += '\n' + stripped_line
            
            if current_key:
                if isinstance(current_value, list):
                    frontmatter[current_key] = current_value
                else:
                    frontmatter[current_key] = current_value.strip() if current_value else ''
            
            remaining_content = '\n'.join(lines[i:]).strip()
            return frontmatter, remaining_content
        
        # 没有 frontmatter
        return {}, content
    
    def generate_post_content(
        self,
        title: str,
        content: str,
        tags: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        date: Optional[datetime] = None,
        published: bool = True,
        catalog: bool = True,
        author: str = 'Shenpotato'
    ) -> str:
        # 先尝试解析内容中的 frontmatter
        existing_frontmatter, remaining_content = self._parse_frontmatter_from_content(content)
        
        if existing_frontmatter:
            # 使用现有的 frontmatter，但确保格式正确（用 --- 包裹）
            frontmatter_lines = ['---']
            for key, value in existing_frontmatter.items():
                if key in ['tags'] and isinstance(value, list):
                    frontmatter_lines.append(f'{key}:')
                    for item in value:
                        frontmatter_lines.append(f'  - {item}')
                elif key in ['categories']:
                    if isinstance(value, list):
                        frontmatter_lines.append(f'{key}: {" ".join(value)}')
                    else:
                        frontmatter_lines.append(f'{key}: {value}')
                else:
                    frontmatter_lines.append(f'{key}: {value}')
            frontmatter_lines.append('---')
            frontmatter = '\n'.join(frontmatter_lines)
            return f'{frontmatter}\n\n{remaining_content}'
        
        # 没有现有的 frontmatter，生成新的
        if date is None:
            date = datetime.now()
        
        frontmatter_lines = [
            '---',
            'layout: post',
            f'title: {title}',
            f'author: {author}',
            f'catalog: {str(catalog).lower()}',
            f'published: {str(published).lower()}',
        ]
        
        if tags:
            frontmatter_lines.append('tags:')
            for tag in tags:
                frontmatter_lines.append(f'  - {tag}')
        
        if categories:
            frontmatter_lines.append(f'categories: {" ".join(categories)}')
        
        frontmatter_lines.append('---')
        frontmatter = '\n'.join(frontmatter_lines)
        
        return f'{frontmatter}\n\n{content}'
    
    def save_post(
        self,
        title: str,
        content: str,
        tags: Optional[List[str]] = None,
        categories: Optional[List[str]] = None,
        date: Optional[datetime] = None,
        published: bool = True,
        overwrite: bool = False
    ) -> str:
        if date is None:
            date = datetime.now()
        
        # 自动获取分类
        final_categories = self.get_category_from_content(title, content, categories)
        print(f'  Using categories: {final_categories}')
        
        category_dir = self.get_category_dir(final_categories)
        filename = self._get_post_filename(title, date)
        filepath = os.path.join(category_dir, filename)
        
        if os.path.exists(filepath) and not overwrite:
            raise FileExistsError(f'Post already exists: {filepath}')
        
        post_content = self.generate_post_content(
            title=title,
            content=content,
            tags=tags,
            categories=final_categories,
            date=date,
            published=published
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(post_content)
        
        return filepath
    
    def post_exists(self, title: str, date: Optional[datetime] = None) -> bool:
        if date is None:
            date = datetime.now()
        
        filename = self._get_post_filename(title, date)
        for root, _, files in os.walk(self.posts_dir):
            if filename in files:
                return True
        return False
