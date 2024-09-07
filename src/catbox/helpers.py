import requests
from .exceptions import CatboxError, TimeoutError, ConnectionError, HTTPError

def upload_file(file_path, timeout=30, userhash=None):
    """
    Upload file to Catbox. If userhash is provided, the upload will be authenticated.
    
    :param file_path: Path to the file to upload.
    :param timeout: Timeout in seconds for the upload request.
    :param userhash: Optional userhash for authenticated upload.
    :return: URL of the uploaded file on Catbox.
    """
    try:
        with open(file_path, 'rb') as file:
            files = {'fileToUpload': file}
            data = {'reqtype': 'fileupload'}
            
            if userhash:
                data['userhash'] = userhash  
                
            response = requests.post("https://catbox.moe/user/api.php", files=files, data=data, timeout=timeout)
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

def upload_to_litterbox(file_path, time='1h', timeout=30):
    """
    Upload file to Litterbox (temporary storage).
    
    :param file_path: Path to the file to upload.
    :param time: Duration for which the file will be available. Options: '1h', '12h', '24h', '72h'.
    :param timeout: Timeout in seconds for the upload request.
    :return: URL of the uploaded file on Litterbox.
    """
    try:
        with open(file_path, 'rb') as file:
            files = {'fileToUpload': file}
            data = {'reqtype': 'fileupload', 'time': time}
            response = requests.post("https://litterbox.catbox.moe/resources/internals/api.php", files=files, data=data, timeout=timeout)
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

def upload_album(file_paths, timeout=30, userhash=None):
    """
    Upload multiple files as an album to Catbox and return their links.
    
    :param file_paths: List of paths to the files to upload.
    :param timeout: Timeout in seconds for the upload request.
    :param userhash: Optional userhash for authenticated upload.
    :return: List of URLs of the uploaded files on Catbox.
    """
    uploaded_links = []
    try:
        for file_path in file_paths:
            with open(file_path, 'rb') as file:
                files = {'fileToUpload': file}
                data = {'reqtype': 'fileupload'}
                
                if userhash:
                    data['userhash'] = userhash

                response = requests.post("https://catbox.moe/user/api.php", files=files, data=data, timeout=timeout)
                response.raise_for_status()
                uploaded_links.append(response.text.strip())
        return uploaded_links
    except requests.exceptions.Timeout:
        raise TimeoutError(f"Album upload timed out after {timeout} seconds.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Failed to connect to Catbox. The server might be down.")
    except requests.exceptions.HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        raise CatboxError(f"An error occurred: {str(e)}")

def delete_files(files, userhash):
    """
    Delete multiple files from Catbox using userhash.
    
    :param files: List of filenames to delete from Catbox.
    :param userhash: userhash for authenticated deletion.
    """
    try:
        data = {
            'reqtype': 'deletefiles',
            'userhash': userhash,
            'files': ' '.join(files)
        }
        response = requests.post("https://catbox.moe/user/api.php", data=data)
        response.raise_for_status()
        print(f"Deleted files: {files}")
    except requests.RequestException as e:
        raise CatboxError(f"Failed to delete files: {str(e)}")

def create_album(files, title, description, userhash):
    """
    Create a new album on Catbox with the specified files.
    
    :param files: List of filenames that have been uploaded to Catbox.
    :param title: Title of the album.
    :param description: Description of the album.
    :param userhash: userhash for authenticated album creation.
    :return: Shortcode of the created album.
    """
    try:
        data = {
            'reqtype': 'createalbum',
            'userhash': userhash,
            'title': title,
            'desc': description,
            'files': ' '.join(files)
        }
        response = requests.post("https://catbox.moe/user/api.php", data=data)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        raise CatboxError(f"Failed to create album: {str(e)}")

def edit_album(shortcode, files, title, description, userhash):
    """
    Edit an existing album on Catbox.
    
    :param shortcode: The short alphanumeric code of the album.
    :param files: List of filenames to be part of the album.
    :param title: Title of the album.
    :param description: Description of the album.
    :param userhash: userhash for authenticated album editing.
    """
    try:
        data = {
            'reqtype': 'editalbum',
            'userhash': userhash,
            'short': shortcode,
            'title': title,
            'desc': description,
            'files': ' '.join(files)
        }
        response = requests.post("https://catbox.moe/user/api.php", data=data)
        response.raise_for_status()
        print(f"Successfully edited album {shortcode}")
    except requests.RequestException as e:
        raise CatboxError(f"Failed to edit album: {str(e)}")

def delete_album(shortcode, userhash):
    """
    Delete an album from Catbox.
    
    :param shortcode: The short alphanumeric code of the album.
    :param userhash: userhash for authenticated album deletion.
    """
    try:
        data = {
            'reqtype': 'deletealbum',
            'userhash': userhash,
            'short': shortcode
        }
        response = requests.post("https://catbox.moe/user/api.php", data=data)
        response.raise_for_status()
        print(f"Successfully deleted album {shortcode}")
    except requests.RequestException as e:
        raise CatboxError(f"Failed to delete album: {str(e)}")