# Catbox Uploader

Catbox Uploader is a simple Python library to upload files and URLs to [Catbox.moe](https://catbox.moe), including its temporary storage feature, **Litterbox**.

## Installation

```bash
pip install catbox-uploader
```

## Usage

### Upload a File to Catbox

You can upload files to **Catbox.moe** using the `upload_file` method. The file will be stored permanently.

```python
from catbox import CatboxUploader

uploader = CatboxUploader()
link = uploader.upload_file('path/to/your/image.png')
print(f'Uploaded file link: {link}')
```

### Upload a File to Litterbox (Temporary Storage)

Litterbox allows you to upload files for a temporary period, after which the files will be deleted automatically. Use the `upload_to_litterbox` method to upload files with a specified expiration time.

**Available expiration times**:
- `1h`: 1 hour
- `12h`: 12 hours
- `24h`: 24 hours
- `72h`: 3 days

Example of uploading a file to Litterbox for 24 hours:

```python
from catbox import CatboxUploader

uploader = CatboxUploader()
link = uploader.upload_to_litterbox('path/to/your/image.png', time='24h')
print(f'Uploaded file link (available for 24 hours): {link}')
```

### Upload Multiple Files as an Album to Catbox

You can upload multiple files as an album to **Catbox.moe** using the `upload_album` method. This allows you to upload several files at once, and it will return the links for all uploaded files.

```python
from catbox import CatboxUploader

uploader = CatboxUploader()
file_paths = ['file1.jpg', 'file2.jpg', 'file3.jpg']
links = uploader.upload_album(file_paths)
for link in links:
    print(f'Uploaded file link: {link}')
```

### Upload a URL to Catbox

If you want to upload a file via a URL to **Catbox**, you can use the `upload_url` method.

```python
from catbox import CatboxUploader

uploader = CatboxUploader()
link = uploader.upload_url('https://example.com/image.png')
print(f'Uploaded URL link: {link}')
```

## Error Handling

The library comes with built-in exception handling to manage common errors such as timeouts, connection issues, or HTTP errors.

### Handling Timeout

If the upload takes too long and exceeds the specified timeout, a `TimeoutError` will be raised.

```python
from catbox import CatboxUploader, TimeoutError

uploader = CatboxUploader()
try:
    link = uploader.upload_file('path/to/your/image.png', timeout=10)
    print(f'Uploaded file link: {link}')
except TimeoutError:
    print("The upload took too long and timed out.")
```

### Handling Connection Issues

If there's a problem connecting to the **Catbox.moe** or **Litterbox** server, a `ConnectionError` will be raised.

```python
from catbox import CatboxUploader, ConnectionError

uploader = CatboxUploader()
try:
    link = uploader.upload_file('path/to/your/image.png')
    print(f'Uploaded file link: {link}')
except ConnectionError:
    print("Failed to connect to the server.")
```

### Handling HTTP Errors

In case of HTTP errors (such as 404 or 500), an `HTTPError` will be raised.

```python
from catbox import CatboxUploader, HTTPError

uploader = CatboxUploader()
try:
    link = uploader.upload_file('path/to/your/image.png')
    print(f'Uploaded file link: {link}')
except HTTPError as he:
    print(f"HTTP error occurred: {he}")
```

### Other Errors

For other unexpected errors, a general `CatboxError` will be raised.

```python
from catbox import CatboxUploader, CatboxError

uploader = CatboxUploader()
try:
    link = uploader.upload_file('path/to/your/image.png')
    print(f'Uploaded file link: {link}')
except CatboxError as e:
    print(f"An error occurred: {e}")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
