"""
Commit.py
---------
Purpose: Represents a commit.

Design Pattern:
- None

SOLID Principles:
- SRP: Encapsulates commit data.
"""

import datetime
import hashlib

class Commit:
    def __init__(self, message: str, files: dict, parent: str = None):
        self.message = message
        self.files = files
        self.parent = parent
        self.timestamp = datetime.datetime.now()
        self.hash = self.compute_hash()

    def compute_hash(self):
        raw = str(self.message) + str(self.files) + (self.parent or '') + str(self.timestamp)
        return hashlib.sha1(raw.encode()).hexdigest()
