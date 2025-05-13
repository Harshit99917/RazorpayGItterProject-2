# Gitter - A Git-like CLI Version Control Tool

## ✅ Overview

Gitter is a simplified Git-style CLI built in Python that supports:
- `init` – initialize repo
- `add` – stage files
- `commit` – save snapshot
- `status` – view file status
- `log` – view commit history

---

## ✅ Architecture

- `models/`        → file blobs and commit objects
- `services/`      → business logic for each command
- `repositories/`  → persistent file I/O abstraction
- `commands/`      → Command pattern wrappers
- `command_router/`→ Factory to route CLI input
- `main.py`        → Parses CLI and dispatches commands

---

## ✅ Design Principles

| Principle | Applied In |
|----------|-------------|
| SRP      | One job per file/class |
| OCP      | Add commands without changing main.py |
| LSP      | All command classes implement `.execute()` |
| ISP      | `BaseServiceInterface`, `BaseCommand` |
| DIP      | Services get repos injected from main |

---

## ✅ Patterns Used

- **Singleton** – Repositories & FileManager
- **Factory** – CommandRouter
- **Command Pattern** – CLI commands
- **Strategy** – (Ready for diff service)
- **Interface** – BaseServiceInterface, BaseCommand

---

## ✅ Setup & Run

```bash

### 🔧 Setting Up Virtual Environment (Linux / macOS / Windows)

1. Create the virtual environment  
Linux/macOS: `python3 -m venv venv`  
Windows: `python -m venv venv`

2. Activate the virtual environment  
Linux/macOS: `source venv/bin/activate`  
Windows: `venv\\Scripts\\activate`

3. Install dependencies  
`pip3 install -r requirements.txt`

4. Deactivate when done  
`deactivate`


# to use gitter as alias 
alias gitter='python pwd'
#  commands which we can use 
gitter init
gitter add .
gitter commit -m "Initial commit"
gitter status
gitter log
gitter tests/
```

---



## 🧪 Testing

Tests are available in `/tests/` folder using `pytest`.
pytest tests/

---

## 📜 License

MIT
