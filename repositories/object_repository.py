"""
ObjectRepository.py
-------------------
Purpose: Saves and retrieves blobs from disk.

Design Pattern:
- Singleton

SOLID Principles:
- SRP: Manages only blob content storage.
"""

import os

class ObjectRepository:
    _instance = None

    def __new__(cls, file_manager):
        if cls._instance is None:
            cls._instance = super(ObjectRepository, cls).__new__(cls)
            cls._instance.file_manager = file_manager
            cls._instance.objects_path = os.path.join(file_manager.repo_path, "objects")
        return cls._instance

    def save_blob(self, blob):
        path = os.path.join(self.objects_path, blob.hash)
        self.file_manager.write_file(path, blob.content)

    def get_blob(self, hash):
        path = os.path.join(self.objects_path, hash)
        return self.file_manager.read_file(path)
