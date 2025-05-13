"""
CommitRepository.py
-------------------
Purpose: Handles saving and loading of commits from .gitter/objects/

Design Pattern:
- Singleton

SOLID Principles:
- SRP: Manages commit storage only.
"""

import os
import json
import logging
from models.commit import Commit

class CommitRepository:
    _instance = None

    def __new__(cls, file_manager):
        if cls._instance is None:
            cls._instance = super(CommitRepository, cls).__new__(cls)
            cls._instance.file_manager = file_manager
            cls._instance.objects_path = os.path.join(file_manager.repo_path, "objects")
            cls._instance.head_path = os.path.join(file_manager.repo_path, "HEAD")
        return cls._instance

    def save_commit(self, commit):
        path = os.path.join(self.objects_path, commit.hash)
        self.file_manager.write_json(path, commit.__dict__)

    def get_commit(self, hash):
        path = os.path.join(self.objects_path, hash)
        data = self.file_manager.read_json(path)
        if not data:
            return None
        return Commit(data['message'], data['files'], data['parent'])

    def get_head_commit(self):
        branch = self.get_current_branch()
        branch_path = os.path.join(self.file_manager.repo_path, branch)
        if not os.path.exists(branch_path):
            return None
        commit_hash = self.file_manager.read_file(branch_path).strip()
        return self.get_commit(commit_hash)

    def get_current_branch(self):
        return self.file_manager.read_file(self.head_path).strip()
