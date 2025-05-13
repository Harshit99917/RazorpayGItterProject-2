"""
main.py
--------
Purpose:
- CLI entry point: parses arguments and routes them to the proper command object.

Design Pattern:
- ✅ Command Pattern (each command has `.execute()`)
- ✅ Dependency Injection (via service factory)
- ✅ Factory Pattern (through CommandRouter)

Why:
- Coordinates CLI execution without managing internal logic.
"""




import sys
from service_factory import build_services
from command_router import CommandRouter



def main():
    args = sys.argv[1:]
    if not args:
        print("Run `gitter help` for usage.")
        return

    command = args[0]
    options = args[1:]

    services = build_services()
    cmd_instance = CommandRouter.route(command, options, services)
    if cmd_instance:
        cmd_instance.execute()

if __name__ == "__main__":
    main()
