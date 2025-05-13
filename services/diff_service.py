"""
DiffService.py
--------------
Purpose: Show differences between working directory and HEAD commit.

Design Pattern:
- Strategy (uses difflib)

SOLID:
- SRP: Only handles diff logic
"""

import difflib
import os
from interfaces.base_service import BaseServiceInterface

class DiffService(BaseServiceInterface):
    def __init__(self, file_manager, commit_repo):
        self.file_manager = file_manager
        self.commit_repo = commit_repo

    def execute(self, path=None):
        head_commit = self.commit_repo.get_head_commit()
        if not head_commit:
            print("No commits found.")
            return

        commit_files = head_commit.files
        changed_files = []

        def process_file(file_path, old_content):
            if not os.path.exists(file_path):
                return
            new_content = self.file_manager.read_file(file_path)
            if new_content != old_content:
                old_lines = old_content.splitlines(keepends=True)
                new_lines = new_content.splitlines(keepends=True)
                diff = difflib.unified_diff(
                    old_lines, new_lines,
                    fromfile=f"a/{file_path}",
                    tofile=f"b/{file_path}",
                    lineterm=""
                )
                print("".join(diff))

        if path:
            if os.path.isfile(path):
                if path in commit_files:
                    process_file(path, self.file_manager.read_file(os.path.join(self.file_manager.repo_path, "objects", commit_files[path])))
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for f in files:
                        full_path = os.path.join(root, f)
                        rel_path = os.path.relpath(full_path, ".")
                        if rel_path in commit_files:
                            process_file(rel_path, self.file_manager.read_file(os.path.join(self.file_manager.repo_path, "objects", commit_files[rel_path])))
        else:
            for file_path, hash_val in commit_files.items():
                process_file(file_path, self.file_manager.read_file(os.path.join(self.file_manager.repo_path, "objects", hash_val)))
