from services.log_service import LogService
from commands.base_command import BaseCommand

class LogCommand(BaseCommand):
    def __init__(self, commit_repo):
        self.service = LogService(commit_repo)

    def execute(self):
        self.service.execute()
