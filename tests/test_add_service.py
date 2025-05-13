# from  pytest import pytest
from services.add_service import AddService
from repositories.index_repository import IndexRepository
from repositories.object_repository import ObjectRepository
from file_manager import FileManager

def test_add_service_stages_file(tmp_path):
    fm = FileManager()
    fm.repo_path = tmp_path / ".gitter"
    fm.repo_path.mkdir()
    (fm.repo_path / "objects").mkdir(parents=True, exist_ok=True)

    index_repo = IndexRepository(fm)
    object_repo = ObjectRepository(fm)
    service = AddService(fm, index_repo, object_repo)

    file = tmp_path / "file1.txt"
    file.write_text("data")
    service.execute([str(file)])

    index = index_repo.get_index()
    assert str(file) in index
