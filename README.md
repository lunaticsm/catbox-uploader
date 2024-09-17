# Catbox Uploader

Catbox Uploader is a simple Python library to upload files and URLs to [Catbox.moe](https://catbox.moe), including its temporary storage feature, **Litterbox**, and album management.

## Installation

```bash
pip install catbox-uploader
```

## Usage

### Using Userhash

CatboxUploader supports using a **userhash** directly. You can pass the `userhash` when initializing the `CatboxUploader` and use it for authenticated uploads and album management.

### Initialize with Userhash

```python
from catbox import CatboxUploader

uploader = CatboxUploader(userhash='your_userhash_here')
```

### Initialize without Userhash

```python
from catbox import CatboxUploader

uploader = CatboxUploader()
```

### Upload a File

```python
link = uploader.upload_file('path/to/your/file.jpg')
print(f'Uploaded file: {link}')
```

### Upload a File to Litterbox (Temporary Storage)

Litterbox allows you to upload files for a temporary period, after which the files will be deleted automatically. Use the `upload_to_litterbox` method to upload files with a specified expiration time.

**Available expiration times**:
- `1h`: 1 hour
- `12h`: 12 hours
- `24h`: 24 hours
- `72h`: 3 days

```python
link = uploader.upload_to_litterbox('path/to/your/file.jpg', time='24h')
print(f'Uploaded file (available for 24 hours): {link}')
```

### Upload Multiple Files as an Album

You can upload multiple files as an album to **Catbox.moe** using the `upload_album` method. This allows you to upload several files at once, and it will return the links for all uploaded files.

```python
file_paths = ['file1.jpg', 'file2.jpg', 'file3.jpg']
links = uploader.upload_album(file_paths)
for link in links:
    print(f'Uploaded file link: {link}')
```

### Create and Manage Albums

#### Create an Album

You can create an album with uploaded files, a title, and a description using the `create_album` method:

```python
album_shortcode = uploader.create_album(file_links, "My Album", "This is a test album")
print(f"Album created: https://catbox.moe/c/{album_shortcode}")
```

#### Edit an Album

You can edit an album by changing its title, description, or the files it contains:

```python
uploader.edit_album(album_shortcode, file_links, "Updated Album Title", "Updated description")
```

#### Delete an Album

You can delete an album by its shortcode:

```python
uploader.delete_album(album_shortcode)
```

### Error Handling

The library comes with built-in exception handling to manage common errors such as timeouts, connection issues, or HTTP errors.

### Handling Timeout

If the upload takes too long and exceeds the specified timeout, a `TimeoutError` will be raised.

```python
from catbox import CatboxUploader, TimeoutError

uploader = CatboxUploader(userhash='your_userhash_here')
try:
    link = uploader.upload_file('path/to/your/file.jpg', timeout=10)
    print(f'Uploaded file: {link}')
except TimeoutError:
    print("The upload took too long and timed out.")
```

### Handling Connection Issues

If there's a problem connecting to the **Catbox.moe** or **Litterbox** server, a `ConnectionError` will be raised.

```python
from catbox import CatboxUploader, ConnectionError

uploader = CatboxUploader(userhash='your_userhash_here')
try:
    link = uploader.upload_file('path/to/your/file.jpg')
    print(f'Uploaded file: {link}')
except ConnectionError:
    print("Failed to connect to the server.")
```

### Handling HTTP Errors

In case of HTTP errors (such as 404 or 500), an `HTTPError` will be raised.

```python
from catbox import CatboxUploader, HTTPError

uploader = CatboxUploader(userhash='your_userhash_here')
try:
    link = uploader.upload_file('path/to/your/file.jpg')
    print(f'Uploaded file: {link}')
except HTTPError as he:
    print(f"HTTP error occurred: {he}")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
