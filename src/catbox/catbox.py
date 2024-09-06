import requests
from .exceptions import CatboxError, FileNotFoundError, TimeoutError, ConnectionError, HTTPError

class CatboxUploader:
    def __init__(self):
        self.api_url = 'https://catbox.moe/user/api.php'
        self.litterbox_url = 'https://litterbox.catbox.moe/resources/internals/api.php'

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

    def upload_to_litterbox(self, file_path, time='1h', timeout=30):
        """
        Upload file to Litterbox (temporary storage) and return the link.
        
        :param file_path: Path to the file to upload.
        :param time: Duration for which the file will be available. Options: '1h', '12h', '24h', '72h'.
        :param timeout: Timeout in seconds for the upload request.
        :return: URL of the uploaded file on Litterbox.
        """
        try:
            with open(file_path, 'rb') as file:
                files = {'fileToUpload': file}
                data = {'reqtype': 'fileupload', 'time': time}
                response = requests.post(self.litterbox_url, files=files, data=data, timeout=timeout)
                response.raise_for_status()
                return response.text.strip()
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Upload to Litterbox timed out after {timeout} seconds.")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Failed to connect to Litterbox. The server might be down.")
        except requests.exceptions.HTTPError as http_err:
            raise HTTPError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as e:
            raise CatboxError(f"An error occurred: {str(e)}")