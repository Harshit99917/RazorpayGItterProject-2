from pathlib import Path
from services.init_service import InitService
from file_manager import FileManager

def test_init_service_creates_gitter_structure(tmp_path):
    fm = FileManager()
   
    fm.repo_path = tmp_path/".gitter"  # ✅ uses Path, not os.path.join
    service = InitService(fm)
    service.execute()

    assert (fm.repo_path / "index").exists()
    assert (fm.repo_path / "objects").exists()
    assert (fm.repo_path / "refs").exists()
