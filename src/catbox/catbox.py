from .helpers import upload_file, upload_to_litterbox, upload_album, delete_files, create_album, edit_album, delete_album
from .exceptions import CatboxError

class CatboxUploader:
    def __init__(self, userhash=None):
        """
        Initialize CatboxUploader with optional userhash (similar to API key).
        
        :param userhash: A string containing the userhash for authenticated uploads and album management.
        """
        self.userhash = userhash
    
    def upload_file(self, file_path, timeout=30):
        return upload_file(file_path, timeout, self.userhash)

    def upload_to_litterbox(self, file_path, time='1h', timeout=30):
        return upload_to_litterbox(file_path, time, timeout)

    def upload_album(self, file_paths, timeout=30):
        return upload_album(file_paths, timeout, self.userhash)

    def delete_files(self, files):
        if not self.userhash:
            raise CatboxError("Userhash is required to delete files.")
        return delete_files(files, self.userhash)

    def create_album(self, files, title, description):
        if not self.userhash:
            raise CatboxError("Userhash is required to create an album.")
        return create_album(files, title, description, self.userhash)

    def edit_album(self, shortcode, files, title, description):
        if not self.userhash:
            raise CatboxError("Userhash is required to edit an album.")
        return edit_album(shortcode, files, title, description, self.userhash)

    def delete_album(self, shortcode):
        if not self.userhash:
            raise CatboxError("Userhash is required to delete an album.")
        return delete_album(shortcode, self.userhash)