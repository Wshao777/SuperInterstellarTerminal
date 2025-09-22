import gspread
from oauth2client.service_account import ServiceAccountCredentials

try:
    from . import config
except ImportError:
    print("FATAL ERROR: Configuration file not found.")
    print("Please copy 'app/config_template.py' to 'app/config.py' and fill in your settings.")
    exit(1)

# --- System Services ---

def get_system_status():
    """A placeholder service function."""
    return {"status": "All systems nominal"}

# --- Google Sheets Services ---

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

def get_google_sheet():
    """
    Connects to Google Sheets and returns a specific worksheet.
    """
    settings = config.settings
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            settings.GOOGLE_CREDENTIALS_FILE, SCOPE
        )
        client = gspread.authorize(creds)
        sheet = client.open(settings.GOOGLE_SHEET_NAME).sheet1  # Get the first sheet
        return sheet
    except FileNotFoundError:
        print(f"ERROR: Google credentials file not found at '{settings.GOOGLE_CREDENTIALS_FILE}'")
        return None
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"ERROR: Google Sheet with name '{settings.GOOGLE_SHEET_NAME}' not found.")
        return None

def get_all_orders_from_sheet():
    """
    Fetches all records from the Google Sheet.
    """
    sheet = get_google_sheet()
    if sheet:
        return sheet.get_all_records()
    return []
