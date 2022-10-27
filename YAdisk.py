from pprint import pprint

import requests


class YaDisk:
    host = 'https://cloud-api.yandex.net:443'
    
    def __init__(self, token: str):
        self.token = token
        
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }    

    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        pprint(response.json())
        
        
    def _get_upload_link(self, path):
        url =  f'{self.host}/v1/disk/resources/upload' 
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, headers=headers, params=params)
        pprint(response.json())
        return response.json().get('href')  
     
        
    def upload(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201: 
            print('Success')
        
        
Yandex_Token = 'y0_AgAAAABloBLcAADLWwAAAADSSbXmrnK5_RNuSN643aWGDXmLGFNXI8U' 

if __name__ == '__main__':
    yadisk = YaDisk(Yandex_Token)
    yadisk.upload('/CHM Villas.jpg', 'CHM Villas.jpg')
    