from commands.base_command import BaseCommand
from services.diff_service import DiffService

class DiffCommand(BaseCommand):
    def __init__(self, file_manager, commit_repo, options):
        self.service = DiffService(file_manager, commit_repo)
        self.options = options

    def execute(self):
        path = self.options[0] if self.options else None
        self.service.execute(path)
