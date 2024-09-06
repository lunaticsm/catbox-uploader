import requests
from .exceptions import CatboxError, FileNotFoundError, TimeoutError, ConnectionError, HTTPError

class CatboxUploader:
    def __init__(self):
        self.api_url = 'https://catbox.moe/user/api.php'

    def upload_file(self, file_path, timeout=30):
        """
        Upload file to Catbox and return the link.
        
        :param file_path: Path to the file to upload.
        :param timeout: Timeout in seconds for the upload request.
        :return: URL of the uploaded file on Catbox.
        """
        try:
            with open(file_path, 'rb') as file:
                files = {'fileToUpload': file}
                data = {'reqtype': 'fileupload'}
                response = requests.post(self.api_url, files=files, data=data, timeout=timeout)
                response.raise_for_status()
                return response.text.strip()
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Upload request timed out after {timeout} seconds.")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Failed to connect to Catbox. The server might be down.")
        except requests.exceptions.HTTPError as http_err:
            raise HTTPError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as e:
            raise CatboxError(f"An error occurred: {str(e)}")

    def upload_url(self, url, timeout=30):
        """
        Upload a URL to Catbox and return the link.
        
        :param url: URL of the file to upload.
        :param timeout: Timeout in seconds for the upload request.
        :return: URL of the uploaded file on Catbox.
        """
        try:
            data = {
                'reqtype': 'urlupload',
                'url': url
            }
            response = requests.post(self.api_url, data=data, timeout=timeout)
            response.raise_for_status()
            return response.text.strip()
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Upload request timed out after {timeout} seconds.")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Failed to connect to Catbox. The server might be down.")
        except requests.exceptions.HTTPError as http_err:
            raise HTTPError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as e:
            raise CatboxError(f"An error occurred: {str(e)}")
