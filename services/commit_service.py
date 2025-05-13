"""
CommitService.py
----------------
Purpose: Creates a new commit from staged and optionally modified files.

Design Pattern:
- None

SOLID Principles:
- SRP: Commits changes
- DIP: Uses injected repositories and file manager
"""

from models.commit import Commit
import os
from interfaces.base_service import BaseServiceInterface

class CommitService(BaseServiceInterface):
    def __init__(self, file_manager, index_repo, commit_repo, branch_repo, object_repo):
        self.file_manager = file_manager
        self.index_repo = index_repo
        self.commit_repo = commit_repo
        self.branch_repo = branch_repo
        self.object_repo = object_repo

    def execute(self, message, auto_stage=False):
        # Step 1: If -a flag is set, stage modified files automatically
        if auto_stage:
            print("yessss_came here")
            last_commit = self.commit_repo.get_head_commit()
            if last_commit:
                for file_path, old_hash in last_commit.files.items():
                    if os.path.exists(file_path):
                        content = self.file_manager.read_file(file_path)
                        new_hash = self.file_manager._instance.__class__.__module__.split('.')[0]  # dummy fallback
                        import hashlib
                        new_hash = hashlib.sha1(content.encode()).hexdigest()
                        if new_hash != old_hash:
                            # Save blob and update index
                            from models.file_blob import FileBlob
                            blob = FileBlob(file_path, content)
                            self.object_repo.save_blob(blob)
                            self.index_repo.stage(file_path, blob.hash)

        # Step 2: Proceed to commit staged files
        staged_files = self.index_repo.get_index()
        if not staged_files:
            print("Nothing to commit.")
            return

        parent_commit = self.commit_repo.get_head_commit()
        parent_hash = parent_commit.hash if parent_commit else None

        commit = Commit(message, staged_files, parent_hash)
        self.commit_repo.save_commit(commit)
        self.branch_repo.update_head(commit.hash)
        self.index_repo.clear()
        print("Changes committed.")
