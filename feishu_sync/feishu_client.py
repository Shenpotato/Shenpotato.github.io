import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

class FeishuClient:
    def __init__(self):
        self.app_id = os.getenv('FEISHU_APP_ID')
        self.app_secret = os.getenv('FEISHU_APP_SECRET')
        self.tenant_access_token = None
        self.token_expire_time = 0
        self.base_url = 'https://open.feishu.cn/open-apis'
    
    def _get_tenant_access_token(self):
        if time.time() < self.token_expire_time - 60:
            return self.tenant_access_token
        
        if not self.app_id or not self.app_secret:
            raise ValueError('FEISHU_APP_ID or FEISHU_APP_SECRET is not set in environment variables')
        
        url = f'{self.base_url}/auth/v3/tenant_access_token/internal'
        payload = {
            'app_id': self.app_id,
            'app_secret': self.app_secret
        }
        
        response = requests.post(url, json=payload)
        
        response.raise_for_status()
        data = response.json()
        
        if 'code' in data and data['code'] != 0:
            raise Exception(f'Feishu API error: code={data["code"]}, msg={data.get("msg", "Unknown error")}')
        
        self.tenant_access_token = data['tenant_access_token']
        self.token_expire_time = time.time() + data['expire']
        return self.tenant_access_token
    
    def _get_headers(self):
        token = self._get_tenant_access_token()
        return {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
    
    def get_root_folder(self):
        url = f'{self.base_url}/drive/explorer/v2/root_folder/meta'
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def list_files_in_folder(self, folder_token, page_size=100):
        url = f'{self.base_url}/drive/v1/files'
        headers = self._get_headers()
        params = {
            'folder_token': folder_token,
            'page_size': page_size,
            'order_by': 'EditedTime'
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_document_info(self, document_id):
        url = f'{self.base_url}/docx/v1/documents/{document_id}'
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def get_document_raw_content(self, document_id):
        url = f'{self.base_url}/docx/v1/documents/{document_id}/raw_content'
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def get_document_blocks(self, document_id, page_size=500):
        url = f'{self.base_url}/docx/v1/documents/{document_id}/blocks'
        headers = self._get_headers()
        params = {
            'page_size': page_size
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def download_media(self, media_token):
        url = f'{self.base_url}/drive/v1/medias/{media_token}/download'
        headers = self._get_headers()
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        return response.content
    
    def download_board_as_image(self, board_token):
        url = f'{self.base_url}/board/v1/whiteboards/{board_token}/download_as_image'
        headers = self._get_headers()
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        return response.content
    
    def get_wiki_node(self, node_token, obj_type=None):
        url = f'{self.base_url}/wiki/v2/spaces/get_node'
        headers = self._get_headers()
        params = {'token': node_token}
        if obj_type:
            params['obj_type'] = obj_type
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def list_wiki_nodes(self, parent_node_token=None, space_id=None, page_size=100):
        url = f'{self.base_url}/wiki/v2/spaces/children'
        headers = self._get_headers()
        params = {'page_size': page_size}
        if parent_node_token:
            params['node_token'] = parent_node_token
        if space_id:
            params['space_id'] = space_id
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
