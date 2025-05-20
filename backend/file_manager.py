import os
import shutil
from datetime import datetime

"""FileManager class, who manages files and folders, with the following functions:

1. list_files function, who returns a list of all the files and folders from a path or an error message if the path does not exist

2. create_file function, who creates a new file in the given path

3. create_folder function, who creates a new folder in the given path or returns an error message if the path does not exist

4. copy function, who copies a file or folder from a source to a destination

5. move function, who moves a file or folder from a source to a destination

6. edit_file function, who edits a file

7. rename function, who renames a file or folder

8. delete_file function, who deletes a file or folder or returns an error message if the path does not exist
"""


class FileManager:
    def list_files(self, path='.'):
        if not os.path.exists(path):
            return {'error': 'Path does not exist'}
        files = []
        for f in os.listdir(path):
            file_info = {
                'name': f,
                'size': os.path.getsize(f),
                'ctime': datetime.fromtimestamp(os.path.getctime(f)).strftime('%Y-%m-%d %H:%M:%S')
            }
            files.append(file_info)
        return files

    def create_file(self, path):
        open(path, 'w').close()
        return {'message': 'File created successfully'}

    def create_folder(self, path):
        os.makedirs(path, exist_ok=True)
        return {'message': 'Folder created successfully'}

    def copy(self, src, dest):
        if not os.path.exists(src):
            return {'error': 'Source path does not exist'}
        shutil.copytree(src, dest) if os.path.isdir(src) else shutil.copy(src, dest)
        return {'message': 'Copied successfully'}

    def move(self, src, dest):
        if not os.path.exists(src):
            return {'error': 'Source path does not exist'}
        shutil.move(src, dest)
        return {'message': 'Moved successfully'}

    def edit_file(self, path, content):
        if not os.path.exists(path):
            return {'error': 'Source path does not exist'}
        with open(path, 'w') as f:
            f.write(content)
        return {'message': 'File edited successfully'}

    def rename(self, old_path, new_path):
        if not os.path.exists(old_path):
            return {'error': 'Old path does not exist'}
        os.rename(old_path, new_path)
        return {'message': f'Renamed {old_path} to {new_path}'}

    def delete(self, path):
        if not os.path.exists(path):
            return {'error': 'Source path does not exist'}
        shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
        return {'message': 'Deleted successfully'}
