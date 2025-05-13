# """
# InitService.py
# --------------
# Purpose: Initializes Gitter repository.

# Design Pattern:
# - Singleton

# SOLID Principles:
# - SRP: Handles only initialization.
# - DIP: Depends on FileManager via injection.
# """

# import os
# import logging
# from interfaces.base_service import BaseServiceInterface

# # class InitService(BaseServiceInterface):
#     # def __init__(self, file_manager):
#     #     self.file_manager = file_manager

#     # def execute(self):
#     #     try:
#     #         os.makedirs(os.path.join(self.file_manager.repo_path, "objects"), exist_ok=True)
#     #         os.makedirs(os.path.join(self.file_manager.repo_path, "refs"), exist_ok=True)
#     #         self.file_manager.write_file(os.path.join(self.file_manager.repo_path, "HEAD"), "refs/main")
#     #         logging.info("Initialized empty Git repository in .gitter/")
#     #     except Exception as e:
#     #         logging.error(f"Failed to initialize repository: {str(e)}")


# class InitService(BaseServiceInterface):
#     def __init__(self, file_manager):
#         self.file_manager = file_manager

#     def execute(self):
#         repo_path = self.file_manager.repo_path
#         (repo_path / "objects").mkdir(parents=True, exist_ok=True)
#         (repo_path / "refs").mkdir(parents=True, exist_ok=True)
#         index_path = repo_path / "index"
#         self.file_manager.write_json(index_path, {})


"""
InitService.py
--------------
Purpose:
    Sets up a new Gitter repository.

Design Pattern:
    - SRP (Single Responsibility): Only handles initializing the repository.

SOLID Principles:
    - SRP: Dedicated to initializing repo structure.
    - DIP: Depends on abstracted file_manager.

Creates:
    - .gitter/
        - objects/
        - refs/
        - refs/heads/
        - HEAD (file)
        - index (file)
"""

import os
import logging
from interfaces.base_service import BaseServiceInterface

class InitService(BaseServiceInterface):
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def execute(self):
        try:
            repo_path = self.file_manager.repo_path

            # Create .gitter folder structure
            os.makedirs(os.path.join(repo_path, "objects"), exist_ok=True)
            os.makedirs(os.path.join(repo_path, "refs", "heads"), exist_ok=True)

            # Create HEAD pointing to refs/heads/main
            head_path = os.path.join(repo_path, "HEAD")
            if not os.path.exists(head_path):
                self.file_manager.write_file(head_path, "refs/heads/main")

            # Create empty index file
            index_path = os.path.join(repo_path, "index")
            if not os.path.exists(index_path):
                self.file_manager.write_json(index_path, {})

            logging.info("✅ Initialized empty Gitter repository in .gitter/")
        except Exception as e:
            logging.error(f"❌ Failed to initialize repository: {str(e)}")
