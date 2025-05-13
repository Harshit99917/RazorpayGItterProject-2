"""
command_registry.py
--------------------
Purpose:
- Acts as a centralized registry (factory map) for all available CLI commands.
- Each entry returns the correct Command object with required services.

Design Pattern:
- ✅ Factory Pattern (via lambda dispatch)
- 🔁 Supports Open/Closed Principle: Add new commands without changing routing logic

Why:
- Removes `if-else` clutter from CommandRouter
- Makes command addition extensible and pluggable
"""




from commands.init_command import InitCommand
from commands.add_command import AddCommand
from commands.commit_command import CommitCommand
from commands.status_command import StatusCommand
from commands.log_command import LogCommand
from commands.diff_command import DiffCommand
from commands.help_command import HelpCommand

COMMAND_REGISTRY = {
    "init": lambda s, o: InitCommand(s["file_manager"]),
    "add": lambda s, o: AddCommand(s["file_manager"], s["index_repo"], s["object_repo"], o),
    "commit": lambda s, o: CommitCommand(s["file_manager"], s["index_repo"], s["commit_repo"], s["branch_repo"], s["object_repo"], o),
    "status": lambda s, o: StatusCommand(s["file_manager"], s["index_repo"], s["commit_repo"]),
    "log": lambda s, o: LogCommand(s["commit_repo"]),
    "diff": lambda s, o: DiffCommand(s["file_manager"], s["commit_repo"], o),
    "help": lambda s, o: HelpCommand(s["help_service"], o[0] if o else None)
}
