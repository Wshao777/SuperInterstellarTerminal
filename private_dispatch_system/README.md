# Private Dispatch System

This project is a backend service for an AI-powered private dispatch system, designed to integrate with Google Sheets for data handling.

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- `pip` for package installation

### 2. Installation
1.  **Clone the repository** (or download the source code).

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Configuration
1.  **Create your configuration file**:
    The application requires a `config.py` file to store your settings. A template is provided.
    - Copy `app/config_template.py` to a new file named `app/config.py`.
    - **Do not delete the template file.**

2.  **Set up Google Sheets API Credentials**:
    - Follow the instructions in `GOOGLE_SHEETS_SETUP.md` to generate your `service_account.json` credentials file.
    - Place the `service_account.json` file in the **root directory** of this project.

3.  **Edit your configuration**:
    - Open `app/config.py`.
    - Change `GOOGLE_SHEET_NAME` to the exact name of the Google Sheet you want to use.

### 4. Running the Application
Once the installation and configuration are complete, you can run the FastAPI server using `uvicorn`.

From the project's **root directory**, run the following command:
```bash
uvicorn app.main:app --reload
```

- `--reload`: This flag makes the server restart automatically after you make changes to the code. It is useful for development.

The server will start, and you can access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
