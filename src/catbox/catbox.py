import requests
from .exceptions import CatboxError, FileNotFoundError

class CatboxUploader:
    def __init__(self):
        self.api_url = 'https://catbox.moe/user/api.php'

    def upload_file(self, file_path):
        """
        Upload file to Catbox and return the link.
        
        :param file_path: Path to the file to upload.
        :return: URL of the uploaded file on Catbox.
        """
        try:
            try:
                with open(file_path, 'rb') as file:
                    files = {'fileToUpload': file}
                    data = {'reqtype': 'fileupload'}
                    response = requests.post(self.api_url, files=files, data=data)
                    response.raise_for_status()
                    return response.text.strip()
            except FileNotFoundError:
                raise FileNotFoundError(f"File not found: {file_path}")

        except requests.exceptions.RequestException as e:
            raise CatboxError(f"Error uploading file to Catbox: {str(e)}")

    def upload_url(self, url):
        """
        Upload a URL to Catbox and return the link.
        
        :param url: URL of the file to upload.
        :return: URL of the uploaded file on Catbox.
        """
        try:
            data = {
                'reqtype': 'urlupload',
                'url': url
            }
            response = requests.post(self.api_url, data=data)
            response.raise_for_status()
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            raise CatboxError(f"Error uploading URL to Catbox: {str(e)}")
