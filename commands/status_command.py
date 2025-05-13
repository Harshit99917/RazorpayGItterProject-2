from services.status_service import StatusService
from commands.base_command import BaseCommand

class StatusCommand(BaseCommand):
    def __init__(self, file_manager, index_repo, commit_repo):
        self.service = StatusService(file_manager, index_repo, commit_repo)

    def execute(self):
        self.service.execute()
