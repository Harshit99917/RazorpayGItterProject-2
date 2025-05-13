"""
IndexRepository.py
------------------
Purpose: Manages staging area (index file).

Design Pattern:
- Singleton

SOLID Principles:
- SRP: Manages only the index file.
- DIP: Injected file manager dependency.
"""

import os
import json

class IndexRepository:
    _instance = None

    def __new__(cls, file_manager):
        if cls._instance is None:
            cls._instance = super(IndexRepository, cls).__new__(cls)
            cls._instance.file_manager = file_manager
            cls._instance.index_path = os.path.join(file_manager.repo_path, "index")
        return cls._instance

    def stage(self, file_path, blob_hash):
        index = self.get_index()
        index[file_path] = blob_hash
        self.save_index(index)

    def get_index(self):
        return self.file_manager.read_json(self.index_path) or {}

    def save_index(self, index_data):
        self.file_manager.write_json(self.index_path, index_data)

    def clear(self):
        self.file_manager.write_json(self.index_path, {})
