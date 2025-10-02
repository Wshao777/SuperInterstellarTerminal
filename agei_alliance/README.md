# ⚡ Lightning Empire: Agei Alliance ⚡

Welcome, Commander! This is the central repository for the **Lightning Empire: Agei Alliance**, a fully automated, AI-powered system for dispatch, financial monitoring, and security.

---

## 1️⃣ Core Architecture

This project is built as a collection of Python scripts and configuration files designed to be run as scheduled tasks or via webhooks. The core components are:

- **/config.yaml**: The central configuration file for all system parameters.
- **/jules_dispatcher.py**: The main dispatch engine.
- **/revenue_simulator.py**: Simulates revenue and generates reports.
- **/typhoon_alert.py**: Monitors for weather warnings.
- **/tools/**: A collection of scripts for security and development workflows.

---

## 2️⃣ Quick Start

### 1. Installation & Setup
1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure `.env`:**
    - Create a `.env` file based on `.env.example` (to be created).
    - Fill in all required API keys and tokens.

### 2. Running a Task
You can run individual modules directly for testing:
```bash
python jules_dispatcher.py
```

---

## 3️⃣ Development Workflow

### Creating a Pull Request
To maintain code quality and safety, all changes should be submitted via a Pull Request. A helper script is provided to automate this process.

1.  **Make your code changes.**
2.  **Run the `create_pr.sh` script with a commit message:**
    ```bash
    ./tools/create_pr.sh "feat: Add new feature for market analysis"
    ```
- This script will automatically create a new branch, commit your changes, push the branch, and open a Pull Request on GitHub.

---

## 4️⃣ Security Tools

This repository includes a `tools/` directory with scripts to help maintain security:
- **`env_guard.sh`**: Scans your `.env` file for potential hardcoded secrets.
  ```bash
  ./tools/env_guard.sh
  ```
- **`security_ignore.py`**: Scans the project for sensitive files that are not in `.gitignore`.
  ```bash
  python tools/security_ignore.py
  ```