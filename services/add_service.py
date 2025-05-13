"""
AddService.py
-------------
Purpose: Stages files for commit by hashing content and storing blob.

Design Pattern:
- None

SOLID Principles:
- SRP: Adds files to index only.
- DIP: Uses repositories and file manager via injection.

Improvements:
- Could have made abtract class for addService and strategy  pattern we would have used to achieve it the way we did in commit
"""



import os
import glob
import logging
from models.file_blob import FileBlob
from interfaces.base_service import BaseServiceInterface

class AddService(BaseServiceInterface):
    def __init__(self, file_manager, index_repo, object_repo):
        self.file_manager = file_manager
        self.index_repo = index_repo
        self.object_repo = object_repo

    def execute(self, patterns):
        try:
            files_to_add = []

            for pattern in patterns:
                if "*" in pattern:
                    files_to_add.extend(glob.glob(pattern, recursive=True))
                elif pattern == ".":
                    for root, _, files in os.walk("."):
                        # Skip ignored folders
                        if any(part in root for part in [".gitter", "venv", "__pycache__"]):
                            continue
                        for f in files:
                            files_to_add.append(os.path.join(root, f))
                else:
                    files_to_add.append(pattern)

            # Define extensions and filenames to skip
            ignored_extensions = {".exe", ".dll", ".pyc", ".log", ".class", ".zip", ".tar", ".gz"}
            ignored_filenames = {".DS_Store", "Thumbs.db"}

            for file_path in files_to_add:
                if not os.path.isfile(file_path):
                    continue

                normalized = os.path.normpath(file_path)
                parts = normalized.split(os.sep)

                # Skip if inside ignored folders
                if any(part in {"venv", ".gitter", "__pycache__"} for part in parts):
                    continue

                # Skip system/binary files
                if os.path.basename(file_path) in ignored_filenames or os.path.splitext(file_path)[1] in ignored_extensions:
                    logging.warning(f"Skipped ignored or binary file: {file_path}")
                    continue

                try:
                    content = self.file_manager.read_file(file_path)
                    if not content.strip():
                        logging.warning(f"Skipped empty file: {file_path}")
                        continue

                    blob = FileBlob(file_path, content)
                    self.object_repo.save_blob(blob)
                    self.index_repo.stage(file_path, blob.hash)
                    logging.info(f"Staged: {file_path}")

                except Exception as e:
                    logging.warning(f"Skipped unreadable or binary file: {file_path} - {str(e)}")

            logging.info("✅ Files staged successfully.")
        except Exception as e:
            logging.error(f"❌ Failed to add files: {str(e)}")