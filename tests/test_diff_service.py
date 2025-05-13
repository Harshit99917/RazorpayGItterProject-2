# import pytest
from services.diff_service import DiffService
from repositories.commit_repository import CommitRepository
from models.commit import Commit
from file_manager import FileManager
from datetime import datetime

def test_diff_service_shows_change(tmp_path, capsys):
    fm = FileManager()
    fm.repo_path = tmp_path / ".gitter"
    fm.repo_path.mkdir()
    (fm.repo_path / "objects").mkdir(parents=True, exist_ok=True)

    commit_repo = CommitRepository(fm)
    file = tmp_path / "sample.txt"
    file.write_text("original content")

    obj_file = fm.repo_path / "objects" / "abc"
    obj_file.write_text("original content")
    commit = Commit("c1", {"sample.txt": "abc"},None)
    commit_repo.save_commit(commit)


    file.write_text("changed content")

    service = DiffService(fm, commit_repo)
    service.execute("sample.txt")


