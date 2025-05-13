"""
FileBlob.py
-----------
Purpose: Represents a file's snapshot (content + hash).

Design Pattern:
- None

SOLID Principles:
- SRP: Represents a single blob.
"""

import hashlib

class FileBlob:
    def __init__(self, file_path: str, content: str):
        self.file_path = file_path
        self.content = content
        self.hash = self.compute_hash()

    def compute_hash(self):
        return hashlib.sha1(self.content.encode()).hexdigest()
