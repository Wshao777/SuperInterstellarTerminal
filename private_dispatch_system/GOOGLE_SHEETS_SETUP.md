# How to Set Up Google Sheets API Access

This system requires a Google Cloud service account to access your Google Sheet data securely. Follow these steps to generate the necessary `service_account.json` credentials file.

## Steps

1.  **Go to the Google Cloud Console:**
    Navigate to the [Google Cloud Console](https://console.cloud.google.com/).

2.  **Create a New Project:**
    If you don't have one already, create a new project.

3.  **Enable APIs:**
    - In the project dashboard, go to "APIs & Services" > "Library".
    - Search for and enable the **Google Drive API**.
    - Search for and enable the **Google Sheets API**.

4.  **Create a Service Account:**
    - Go to "APIs & Services" > "Credentials".
    - Click "Create Credentials" and select "Service Account".
    - Give the service account a name (e.g., "Private Dispatch Bot") and a description.
    - Click "Create and Continue".
    - For "Role", select "Project" > "Viewer". Click "Continue".
    - Skip step 3 ("Grant users access to this service account"). Click "Done".

5.  **Generate a JSON Key:**
    - In the "Credentials" screen, find the service account you just created.
    - Click on the service account's email address.
    - Go to the "Keys" tab.
    - Click "Add Key" > "Create new key".
    - Select **JSON** as the key type and click "Create".
    - A JSON file will be downloaded to your computer. **This is your credentials file. Keep it safe and do not commit it to version control.**

6.  **Place the Credentials File:**
    - Rename the downloaded file to `service_account.json`.
    - Place this file in the root directory of this project (`private_dispatch_system/`).

7.  **Share Your Google Sheet:**
    - Open the Google Sheet you want the system to access.
    - Click the "Share" button in the top right corner.
    - Copy the service account's email address (from the "Credentials" page in the Google Cloud Console, it looks like `...gserviceaccount.com`).
    - Paste the email address into the "Share with people and groups" field.
    - Give the service account "Editor" access.
    - Click "Send".

Your system is now configured to securely access the Google Sheet.
