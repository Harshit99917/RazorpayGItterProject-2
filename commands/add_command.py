from services.add_service import AddService
from commands.base_command import BaseCommand

class AddCommand(BaseCommand):
    def __init__(self, file_manager, index_repo, object_repo, options):
        self.service = AddService(file_manager, index_repo, object_repo)
        self.options = options

    def execute(self):
        self.service.execute(self.options)
