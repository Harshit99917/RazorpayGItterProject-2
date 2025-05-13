from commands.base_command import BaseCommand

class HelpCommand(BaseCommand):
    def __init__(self, help_service, command=None):
        self.service = help_service
        self.command = command

    def execute(self):
        self.service.execute(self.command)
