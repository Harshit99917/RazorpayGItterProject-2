"""
BranchRepository.py
-------------------
Purpose: Manages branch metadata and HEAD pointer.

Design Pattern:
- Singleton

SOLID Principles:
- SRP: Handles HEAD and branch pointers.
"""

import os
import logging

class BranchRepository:
    _instance = None

    def __new__(cls, file_manager):
        if cls._instance is None:
            cls._instance = super(BranchRepository, cls).__new__(cls)
            cls._instance.file_manager = file_manager
            cls._instance.head_path = os.path.join(file_manager.repo_path, "HEAD")
        return cls._instance


    def update_head(self, commit_hash):
        current_branch = self.file_manager.read_file(self.head_path).strip()
        branch_path = os.path.join(self.file_manager.repo_path, current_branch)
        self.file_manager.write_file(branch_path, commit_hash)
        logging.info(f"Updated HEAD to commit {commit_hash}")
