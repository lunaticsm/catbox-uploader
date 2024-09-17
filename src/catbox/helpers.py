import requests
from io import BytesIO
import os
from .exceptions import CatboxError, TimeoutError, ConnectionError, HTTPError

def upload_file(file_path_or_bytes, timeout=30, userhash=None):
    """
    Upload file to Catbox. Supports both file paths and BytesIO objects.
    
    :param file_path_or_bytes: Path to the file to upload or a BytesIO object.
    :param timeout: Timeout in seconds for the upload request.
    :param userhash: Optional userhash for authenticated upload.
    :return: URL of the uploaded file on Catbox.
    """
    try:
        if isinstance(file_path_or_bytes, str):
            files = {'fileToUpload': open(file_path_or_bytes, 'rb')}
        else:
            raise CatboxError("Only file paths are supported in this version.")

        data = {'reqtype': 'fileupload'}
        if userhash:
            data['userhash'] = userhash

        response = requests.post("https://catbox.moe/user/api.php", files=files, data=data, timeout=timeout)

        if response.status_code != 200 or not response.text:
            raise CatboxError("Failed to upload file to Catbox.")
        
        return response.text.strip()

    except requests.exceptions.Timeout:
        raise TimeoutError(f"Upload request timed out after {timeout} seconds.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Failed to connect to Catbox.")
    except requests.exceptions.RequestException as e:
        raise CatboxError(f"An error occurred: {str(e)}")
    finally:
        if isinstance(file_path_or_bytes, str):
            files['fileToUpload'].close()

def upload_to_litterbox(file_path_or_bytes, file_name="file.png", time='1h', timeout=30):
    """
    Upload file to Litterbox (temporary storage). Supports both file paths and BytesIO objects.
    
    :param file_path_or_bytes: Path to the file to upload or a BytesIO object.
    :param file_name: Name of the file with extension (e.g., file.png).
    :param time: Duration for which the file will be available. Options: '1h', '12h', '24h', '72h', '1w'.
    :param timeout: Timeout in seconds for the upload request.
    :return: URL of the uploaded file on Litterbox.
    """
    try:
        if isinstance(file_path_or_bytes, BytesIO):
            files = {'fileToUpload': (file_name, file_path_or_bytes, 'application/octet-stream')}
        else:
            with open(file_path_or_bytes, 'rb') as file:
                files = {'fileToUpload': (file_name, file)}
        
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

def upload_album(file_paths_or_bytes_list, timeout=30, userhash=None):
    """
    Upload multiple files as an album to Catbox and return their links. Supports both file paths and BytesIO objects.
    
    :param file_paths_or_bytes_list: List of file paths or BytesIO objects.
    :param timeout: Timeout in seconds for the upload request.
    :param userhash: Optional userhash for authenticated upload.
    :return: List of URLs of the uploaded files on Catbox.
    """
    uploaded_links = []
    try:
        for file_path_or_bytes in file_paths_or_bytes_list:
            if isinstance(file_path_or_bytes, BytesIO):
                files = {'fileToUpload': ('file.png', file_path_or_bytes, 'application/octet-stream')}
            else:
                with open(file_path_or_bytes, 'rb') as file:
                    files = {'fileToUpload': (file.name, file)}
            
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
