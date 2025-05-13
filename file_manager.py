"""
FileManager.py
--------------
Purpose: Handles all file I/O.

Design Pattern:
- Singleton

SOLID Principles:
- SRP: Dedicated to file access.
"""

import os
import json
import logging
from pathlib import Path

class FileManager:
    _instance = None

    def __new__(cls,repo_path=None):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
            cls._instance.root = Path.cwd()
            cls._instance.repo_path = Path(repo_path) if repo_path else cls._instance.root / ".gitter"
        return cls._instance

    def write_json(self, path, data):
        try:
            with open(path, "w") as f:
                json.dump(data, f, indent=4, default=str)
            logging.info(f"Written JSON to {path}")
        except Exception as e:
            logging.error(f"Failed to write JSON to {path}: {str(e)}")

    def read_json(self, path):
        try:
            if not os.path.exists(path):
                return None
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Failed to read JSON from {path}: {str(e)}")
            return None

    def write_file(self, path, content):
        try:
            with open(path, "w") as f:
                f.write(content)
            logging.info(f"Written file to {path}")
        except Exception as e:
            logging.error(f"Failed to write file {path}: {str(e)}")

    def read_file(self, path):
        try:
            if not os.path.exists(path):
                return ""
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except UnicodeDecodeError:
            logging.warning(f"Skipped binary or non-UTF8 file: {path}")
            return ""
        except Exception as e:
            logging.error(f"Failed to read file {path}: {str(e)}")
            return ""
