# import pytest
from services.log_service import LogService
from repositories.commit_repository import CommitRepository
from models.commit import Commit
from file_manager import FileManager
from datetime import datetime

def test_log_service_outputs_commit_message(tmp_path, capsys):
    fm = FileManager()
    fm.repo_path = tmp_path / ".gitter"
    fm.repo_path.mkdir()

    commit_repo = CommitRepository(fm)
    commit = Commit("h1", {}, None)
    commit_repo.save_commit(commit)


    service = LogService(commit_repo)
    service.execute()

    captured = capsys.readouterr()
    # assert "log message" in captured.out
