from commands.base_command import BaseCommand
from services.commit_service import CommitService
import hashlib

class CommitCommand(BaseCommand):
    def __init__(self, file_manager, index_repo, commit_repo, branch_repo, object_repo, options):
        self.file_manager = file_manager
        self.index_repo = index_repo
        self.commit_repo = commit_repo
        self.branch_repo = branch_repo
        self.object_repo = object_repo
        self.options = self._normalize_options(options)  # ✅ normalize flags

    def _normalize_options(self, options):
        """
        Normalize combined flags like -am into ['-a', '-m']
        """
        normalized = []
        for opt in options:
            if opt.startswith("-") and len(opt) > 2:
                # split -am => -a and -m
                for c in opt[1:]:
                    normalized.append(f"-{c}")
            else:
                normalized.append(opt)
        return normalized

    def extract_commit_message(self):
        message_parts = []
        i = 0
        while i < len(self.options):
            if self.options[i] == "-m" and i + 1 < len(self.options):
                message_parts.append(self.options[i + 1])
                i += 2
            else:
                i += 1
        return "\n\n".join(message_parts)

    def has_auto_stage(self):
        return "-a" in self.options

    def execute(self):
        message = self.extract_commit_message()
        if not message:
            print("❌ Missing commit message. Use: gitter commit -m \"message\"")
            return

        auto_stage = self.has_auto_stage()

        service = CommitService(
            self.file_manager,
            self.index_repo,
            self.commit_repo,
            self.branch_repo,
            self.object_repo
            
        )
        service.execute(message, auto_stage)
