class HelpService:
    def __init__(self):
        self.help_text = {
            "init": (
                "NAME:\n"
                "  init - Create an empty Gitter repository\n\n"
                "SYNOPSIS:\n"
                "  gitter init\n\n"
                "DESCRIPTION:\n"
                "  Initializes a new .gitter directory with the necessary folder structure\n"
                "  including objects, refs, and HEAD pointer. Sets default branch as 'main'.\n"
            ),
            "add": (
                "NAME:\n"
                "  add - Add file contents to the index\n\n"
                "SYNOPSIS:\n"
                "  gitter add <file|pattern>\n"
                "  gitter add .\n"
                "  gitter add *.py\n\n"
                "DESCRIPTION:\n"
                "  Adds specified files or patterns to the staging area (index).\n"
                "  - Supports glob patterns (e.g., *.py)\n"
                "  - `.` recursively stages all files except `.gitter/`, `venv/`, `__pycache__/`\n"
                "  - Skips binary, non-UTF8, unreadable, and empty files\n"
            ),
            "commit": (
                "NAME:\n"
                "  commit - Record changes to the repository\n\n"
                "SYNOPSIS:\n"
                "  gitter commit -m \"<message>\"\n"
                "  gitter commit -am \"<message>\"\n\n"
                "DESCRIPTION:\n"
                "  Commits the current staging area. Supports auto-staging modified files with `-a`.\n\n"
                "  OPTIONS:\n"
                "    -m: Required. Commit message\n"
                "    -a: Optional. Auto-stage all tracked modified files\n\n"
                "  EXAMPLES:\n"
                "    gitter commit -m \"Initial commit\"\n"
                "    gitter commit -am \"Quick fix\"\n"
            ),
            "status": (
                "NAME:\n"
                "  status - Show the working tree status\n\n"
                "SYNOPSIS:\n"
                "  gitter status\n\n"
                "DESCRIPTION:\n"
                "  Shows:\n"
                "    - Changes to be committed (staged)\n"
                "    - Changes not staged (modified)\n"
                "    - Untracked files (new)\n"
            ),
            "log": (
                "NAME:\n"
                "  log - Show commit logs\n\n"
                "SYNOPSIS:\n"
                "  gitter log\n\n"
                "DESCRIPTION:\n"
                "  Displays commit history from the current branch HEAD, showing:\n"
                "    - Commit hash\n"
                "    - Author (user)\n"
                "    - Date\n"
                "    - Message\n"
            ),
            "diff": (
                "NAME:\n"
                "  diff - Show differences between working tree and last commit\n\n"
                "SYNOPSIS:\n"
                "  gitter diff\n"
                "  gitter diff <file_path>\n"
                "  gitter diff <directory>\n\n"
                "DESCRIPTION:\n"
                "  Compares current file(s) with last committed version.\n"
                "  - Unified diff output format\n"
                "  - Supports per-file or per-directory diff\n"
            ),
            "help": (
                "NAME:\n"
                "  help - Show usage for all or a specific command\n\n"
                "SYNOPSIS:\n"
                "  gitter help\n"
                "  gitter help <command>\n\n"
                "DESCRIPTION:\n"
                "  Displays help for available commands or one specific command.\n"
            )
        }

    def execute(self, command=None):
        if not command:
            print("These are common Gitter commands:")
            for cmd in self.help_text:
                desc_line = self.help_text[cmd].splitlines()[1].strip()
                print(f"{cmd:<8} {desc_line}")
        elif command in self.help_text:
            print(self.help_text[command])
        else:
            print(f"No help available for '{command}'")
