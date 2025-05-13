"""
LogService.py
-------------
Purpose: Displays commit history from HEAD.

Design Pattern:
- None

SOLID Principles:
- SRP: Only handles commit listing.
"""
from interfaces.base_service import BaseServiceInterface
class LogService(BaseServiceInterface):
    def __init__(self, commit_repo):
        self.commit_repo = commit_repo

    def execute(self):
        current = self.commit_repo.get_head_commit()
        while current:
            print(f"commit {current.hash}")
            print("Author: user")
            print(f"Date:   {current.timestamp}")
            print(f"{current.message}\n")

            if not current.parent:
                break  # First commit, no parent
            current = self.commit_repo.get_commit(current.parent)
