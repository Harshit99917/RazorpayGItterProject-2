"""
command_router.py
-------------------
Purpose:
- Responsible for routing user input to the appropriate Command object using the COMMAND_REGISTRY.

Design Pattern:
- ✅ Factory Pattern (delegates command instantiation)
- ✅ Command Pattern (returns objects with `.execute()`)

SOLID Principles:
- ✅ Single Responsibility: Only handles routing
- ✅ Open/Closed: Add new command types via registry without changing router logic

Why:
- Keeps routing logic isolated and extensible
"""


from command_registry import COMMAND_REGISTRY

class CommandRouter:
    @staticmethod
    def route(command, options, services):
        command_fn = COMMAND_REGISTRY.get(command)
        if not command_fn:
            print(f"Unknown command: {command}")
            return None
        return command_fn(services, options)
