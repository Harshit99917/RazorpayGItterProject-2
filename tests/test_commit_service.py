import pytest
from services.commit_service import CommitService
from repositories.commit_repository import CommitRepository
from repositories.index_repository import IndexRepository
from repositories.branch_repository import BranchRepository
from repositories.object_repository import ObjectRepository
from file_manager import FileManager
from models.file_blob import FileBlob  # ✅ using correct blob model

def test_commit_service_commits_files(tmp_path):
    # Set up fake .gitter repo
    fm = FileManager()
    fm.repo_path = tmp_path / ".gitter"
    (fm.repo_path / "objects").mkdir(parents=True, exist_ok=True)
    (fm.repo_path / "refs" / "heads").mkdir(parents=True, exist_ok=True)
    (fm.repo_path / "index").write_text("")

    index_repo = IndexRepository(fm)
    object_repo = ObjectRepository(fm)
    commit_repo = CommitRepository(fm)
    branch_repo = BranchRepository(fm)

    # Create and stage a test file
    file = tmp_path / "test.txt"
    file.write_text("content")

    content = file.read_text()
    blob = FileBlob(str(file), content)
    object_repo.save_blob(blob)
    index_repo.stage(str(file), blob.hash)

    # Execute commit
    service = CommitService(fm, index_repo, commit_repo, branch_repo, object_repo)
    service.execute("commit message")  # ✅ pass message as a string

  
   
