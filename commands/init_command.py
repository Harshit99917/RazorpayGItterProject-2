from services.init_service import InitService
from commands.base_command import BaseCommand

class InitCommand(BaseCommand):
    def __init__(self, file_manager):
        self.service = InitService(file_manager)

    def execute(self):
        self.service.execute()
