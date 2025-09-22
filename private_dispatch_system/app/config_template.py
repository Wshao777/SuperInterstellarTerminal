import os

class Settings:
    # Google Sheets settings
    GOOGLE_CREDENTIALS_FILE: str = os.getenv("GOOGLE_CREDENTIALS_FILE", "service_account.json")
    GOOGLE_SHEET_NAME: str = os.getenv("GOOGLE_SHEET_NAME", "DispatchData")

    # App settings
    APP_TITLE: str = "Private Dispatch System"
    APP_DESCRIPTION: str = "AI-powered private dispatch system with manual JKO Pay."
    APP_VERSION: str = "0.1.0"

settings = Settings()
