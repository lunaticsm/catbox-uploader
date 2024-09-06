# Catbox Uploader

Catbox Uploader is a simple Python library to upload files and URLs to [Catbox.moe](https://catbox.moe).

## Installation

```bash
pip install catbox_uploader
```

## Usage

### Upload a file:

```python
from catbox_uploader import CatboxUploader

uploader = CatboxUploader()
link = uploader.upload_file('path/to/your/image.png')
print(f'Uploaded file link: {link}')
```

### Upload a URL:

```python
from catbox_uploader import CatboxUploader

uploader = CatboxUploader()
link = uploader.upload_url('https://example.com/image.png')
print(f'Uploaded URL link: {link}')
```

### Error Handling:

```python
from catbox_uploader import CatboxUploader, CatboxError, FileNotFoundError

uploader = CatboxUploader()
try:
    link = uploader.upload_file('path/to/your/file.png')
except FileNotFoundError as e:
    print(f"File error: {str(e)}")
except CatboxError as e:
    print(f"Catbox upload error: {str(e)}")
```
