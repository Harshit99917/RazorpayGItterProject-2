"""
service_factory.py
--------------------
Purpose:
- Centralized factory function to build all services and repositories used across commands.

Design Pattern:
- ✅ Factory Pattern (creates and injects shared dependencies)
- ✅ Singleton Pattern (applies to FileManager)

SOLID Principles:
- ✅ Single Responsibility: Builds and returns service container
- ✅ Dependency Inversion: High-level modules get services via DI, not by instantiating them directly

Why:
- Keeps `main.py` clean
- Makes service creation reusable and testable
"""



from file_manager import FileManager
from repositories.index_repository import IndexRepository
from repositories.commit_repository import CommitRepository
from repositories.branch_repository import BranchRepository
from repositories.object_repository import ObjectRepository
from services.help_service import HelpService

def build_services():
    fm = FileManager()
    return {
        "file_manager": fm,
        "index_repo": IndexRepository(fm),
        "commit_repo": CommitRepository(fm),
        "branch_repo": BranchRepository(fm),
        "object_repo": ObjectRepository(fm),
        "help_service": HelpService()
    }
