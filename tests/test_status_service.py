# import pytest
from services.status_service import StatusService
from repositories.commit_repository import CommitRepository
from repositories.index_repository import IndexRepository
from models.commit import Commit
from file_manager import FileManager
from datetime import datetime

def test_status_service_detects_staged_file(tmp_path, capsys):
    fm = FileManager()
    fm.repo_path = tmp_path / ".gitter"
    fm.repo_path.mkdir()
    (fm.repo_path / "objects").mkdir(parents=True, exist_ok=True)

    index_repo = IndexRepository(fm)
    commit_repo = CommitRepository(fm)

    file = tmp_path / "f.txt"
    file.write_text("v1")
    index_repo.stage(str(file), "hash1")

    commit = Commit("abc", {}, None)
    commit_repo.save_commit(commit)
  

    service = StatusService(fm, index_repo, commit_repo)
    service.execute()

    captured = capsys.readouterr()
    assert "Changes to be committed" in captured.out
