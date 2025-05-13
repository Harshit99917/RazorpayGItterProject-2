"""
StatusService.py
----------------
Purpose: Displays file status between working directory, index, and HEAD commit.

Design Pattern:
- None

SOLID Principles:
- SRP: Show status of files.
"""

import os
from interfaces.base_service import BaseServiceInterface
import os
from interfaces.base_service import BaseServiceInterface

class StatusService(BaseServiceInterface):
    def __init__(self, file_manager, index_repo, commit_repo):
        self.file_manager = file_manager
        self.index_repo = index_repo
        
        self.commit_repo = commit_repo

    def execute(self):
        index_state = self.index_repo.get_index()
        last_commit = self.commit_repo.get_head_commit()
        commit_files = last_commit.files if last_commit else {}

        to_commit = []
        not_staged = []
        untracked = []

        # Normalize for comparison
        normalized_index = {os.path.normpath(k) for k in index_state}
        normalized_commit = {os.path.normpath(k) for k in commit_files}

        # Files staged but different from last commit
        for file_path, blob_hash in index_state.items():
            if file_path not in commit_files or blob_hash != commit_files[file_path]:
                to_commit.append(file_path)

        # Files changed in working dir but not staged
        for file_path, old_hash in commit_files.items():
            try:
                current_content = self.file_manager.read_file(file_path)
                old_content = self.file_manager.read_file(
                    os.path.join(self.file_manager.repo_path, "objects", old_hash)
                )
                if current_content != old_content and file_path not in index_state:
                    not_staged.append(file_path)
            except Exception:
                continue  # file may be deleted or binary, skip

        # Untracked: in working dir, not in index or commit
        for root, _, files in os.walk("."):
            if any(skip in root for skip in [".gitter", "venv", "__pycache__"]):
                continue
            for f in files:
                path = os.path.join(root, f)
                rel_path = os.path.normpath(os.path.relpath(path, "."))

                if any(skip in rel_path for skip in [".gitter", "venv", "__pycache__"]):
                    continue

                if rel_path not in normalized_index and rel_path not in normalized_commit:
                    untracked.append(rel_path)

        # Output sections

        
        if to_commit:
            print("Changes to be committed:")
            for f in to_commit:
                print(f"  modified: {f}")

        if not_staged:
            print("\nChanges not staged for commit:")
            for f in not_staged:
                print(f"  modified: {f}")

        if untracked:
            print("\nUntracked files:")
            for f in untracked:
                print(f"  {f}")
