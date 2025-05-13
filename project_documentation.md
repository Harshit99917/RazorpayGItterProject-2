# 🧱 Gitter CLI – Project Architecture & Design Overview

---

## 🎯 Objective

Build a Git-like CLI tool named `gitter` that supports:
- `init`, `add`, `commit -m`, `commit -am`
- `status`, `log`, `diff`, `help`

All built using:
- Clean Architecture
- SOLID Principles
- Key Design Patterns (Command, Factory, Singleton, DI)

---

## 🧱 Architecture: 3-Layered Structure

```
main.py
└── Command Layer (CLI)
    └── Service Layer (Use Cases)
        └── Repository Layer (File I/O)
```

---

## 📂 Folder Overview

| Folder          | Purpose |
|------------------|---------|
| `main.py`        | Entry point: routes CLI args to commands |
| `commands/`      | CLI commands mapped via `CommandRouter` |
| `services/`      | Core use cases like staging, committing |
| `repositories/`  | Reads/writes file system (index, commits, blobs) |
| `models/`        | Domain models: Commit, Blob |
| `interfaces/`    | Optional base interfaces for commands/services |
| `file_manager.py`| Singleton I/O handler |
| `command_router.py` | Routes CLI command name to Command instance |

---

## 🔧 Command Layer

Implements the **Command Pattern**

- Each CLI command (like `add`, `commit`) is wrapped in a class
- Implements a uniform `.execute()` method

Example:
```
gitter commit -m "message"
└── CommitCommand.execute()
    └── CommitService.execute()
```

---

## 🔁 Service Layer

Handles **business logic**.

| Service            | Role |
|--------------------|------|
| `AddService`       | Hashes and stages files |
| `CommitService`    | Creates commits (with or without `-a`) |
| `StatusService`    | Shows index vs working dir vs HEAD |
| `LogService`       | Walks parent commits backward |
| `DiffService`      | Shows line-level changes |
| `HelpService`      | Outputs command documentation |
| `InitService`      | Initializes `.gitter/` structure |

Each service:
- Is stateless
- Uses repositories via Dependency Injection (DIP)
- Has **SRP**: one job only

---

## 📦 Repository Layer

Handles **all file persistence**.

| Repository           | Manages                          |
|----------------------|-----------------------------------|
| `IndexRepository`    | `.gitter/index`                  |
| `CommitRepository`   | `.gitter/objects/<hash>`         |
| `BranchRepository`   | `.gitter/refs/main`              |
| `ObjectRepository`   | Blob content files               |

Each repository uses `FileManager` (Singleton) to perform actual I/O.

---

## 🧠 Design Patterns Used

| Pattern       | Applied In             | Purpose |
|---------------|-------------------------|---------|
| Singleton     | `FileManager`           | Global state & config |
| Command       | `Command classes`       | Encapsulate CLI actions |
| Factory       | `CommandRouter`         | CLI dispatch |
| DI / SRP      | All services            | Testability and separation |
| Interface (optional) | `BaseCommand`, `BaseService` | Polymorphism |

---

## 🔀 Data Flow Example: `gitter commit -am "msg"`

1. CLI → `main.py`
2. Routed via `CommandRouter` → `CommitCommand`
3. `CommitCommand.execute()` calls `CommitService.execute()`
4. If `-a`, auto-stage modified files via repo + file hash
5. Build `Commit` model, write to `.gitter/objects/`
6. Update `.gitter/refs/main`
7. Clear index

---

## 🛡️ SOLID Principles in Play

| Principle  | Applied In |
|------------|-------------|
| SRP        | All services and repositories do one thing |
| OCP        | Add new command without touching `main.py` |
| LSP        | All commands follow `.execute()` contract |
| ISP        | Via base interfaces for Commands/Services |
| DIP        | All services depend on injected repos, not hard-coded classes |

---

## 🧪 Test Strategy

- Tests in `/tests/` folder
- Use `pytest`
- Services are unit tested with mocked FileManager or isolated `.gitter` folder

---

## 🗂️ Example Directory Tree

```
gitter_project/
├── main.py
├── command_router.py
├── file_manager.py
├── commands/
│   ├── add_command.py
│   ├── commit_command.py
│   └── ...
├── services/
│   ├── add_service.py
│   ├── commit_service.py
│   └── ...
├── repositories/
│   ├── index_repository.py
│   └── ...
├── models/
│   ├── commit.py
│   ├── file_blob.py
│   └── ...
└── tests/
    ├── test_add.py
    └── ...
```

---



## 🧠 Summary

This project is a fully decoupled CLI architecture modeled after Git:
- ✅ 3-Layer Architecture
- ✅ SOLID-compliant
- ✅ Easily testable
- ✅ Extensible CLI pattern

You can build real-world tooling or evolve this into a GUI-backed Git system from here.
