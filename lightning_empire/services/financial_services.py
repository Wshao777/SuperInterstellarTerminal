import os
import json
import requests
import telegram
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

BANK_CODES = {}

def load_bank_codes():
    """Loads bank codes from the JSON file."""
    global BANK_CODES
    try:
        script_dir = os.path.dirname(__file__)
        json_path = os.path.join(script_dir, '..', 'bank_codes.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            BANK_CODES = json.load(f)
    except FileNotFoundError:
        print("❌ Error: bank_codes.json not found.")

def send_telegram_notify(message, token, chat_id):
    """Sends a message to the specified Telegram chat."""
    if not token or not chat_id: return
    try:
        bot = telegram.Bot(token=token)
        bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')
        print("✅ Telegram notification sent.")
    except Exception as e:
        print(f"❌ Failed to send Telegram notification: {e}")

def send_line_notify(message, token):
    """Sends a message via LINE Notify."""
    if not token: return
    try:
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": f"Bearer {token}"}
        data = {"message": message}
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print("✅ LINE notification sent.")
        else:
            print(f"❌ LINE Notify Error: {response.text}")
    except Exception as e:
        print(f"❌ Failed to send LINE notification: {e}")

def notify_all(message):
    """Sends a notification to all configured channels (Telegram and LINE)."""
    print(f"📢 Sending notification:\n{message}")
    send_telegram_notify(message, os.getenv("COMMAND_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID"))
    send_line_notify(message, os.getenv("LINE_NOTIFY_TOKEN"))

def write_to_sheets(bank_code, account, gross_amount, owner_share, system_share, timestamp, from_bank):
    """Appends a new row to the specified Google Sheet."""
    # This function remains largely the same, just updating parameter names for clarity
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds_path = os.getenv('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)
        sheet_name = os.getenv('GOOGLE_SHEET_NAME', 'LightningEmpireAccounts')
        sheet = client.open(sheet_name).sheet1

        bank_name = BANK_CODES.get(bank_code, bank_code)
        row = [timestamp, bank_name, account, gross_amount, owner_share, system_share, from_bank]
        sheet.append_row(row)
        print("✅ Transaction successfully logged to Google Sheets.")
    except Exception as e:
        print(f"❌ Google Sheets Error: {e}")

def verify_and_process_transfer(bank_code, account, amount, from_platform="未知"):
    """
    Verifies a bank transfer against platform-specific accounts,
    calculates a 25/75 profit split, and logs everything.
    """
    load_bank_codes() # Ensure codes are loaded

    expected_account = None
    if from_platform.lower() == "uber":
        expected_account = os.getenv('BANK_UBER_ACCOUNT')
        if bank_code != os.getenv('BANK_UBER_CODE'):
             notify_all(f"❌ 銀行代碼不符: Uber 平台應對應銀行 {os.getenv('BANK_UBER_CODE')}，收到 {bank_code}。")
             return False
    elif from_platform.lower() == "foodpanda":
        expected_account = os.getenv('BANK_FOODPANDA_ACCOUNT')
        if bank_code != os.getenv('BANK_FOODPANDA_CODE'):
             notify_all(f"❌ 銀行代碼不符: Foodpanda 平台應對應銀行 {os.getenv('BANK_FOODPANDA_CODE')}，收到 {bank_code}。")
             return False

    if account == expected_account:
        bank_name = BANK_CODES.get(bank_code, "未知銀行")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # New 25/75 Profit Split
        owner_share = amount * 0.25
        system_share = amount * 0.75

        msg = (
            f"⚡ <b>Lightning Empire 金流入帳 v3.0</b>\n"
            f"🏦 銀行: {bank_name} ({bank_code})\n"
            f"平台: {from_platform}\n"
            f"💰 總額: {amount:,.2f} NT$\n"
            f"👑 您的收益 (25%): {owner_share:,.2f} NT$\n"
            f"🛡️ 系統分潤 (75%): {system_share:,.2f} NT$\n"
            f"📅 時間: {now}\n\n"
            f"🛡️ 總司令，資金到位！"
        )
        notify_all(msg)

        write_to_sheets(bank_code, account, amount, owner_share, system_share, now, from_platform)
        return True
    else:
        bank_name = BANK_CODES.get(bank_code, f"代碼 {bank_code}")
        error_msg = f"❌ 帳戶不符: {from_platform} 平台收到一筆轉帳至 {bank_name}，但帳號 `{account}` 與設定不符。"
        notify_all(error_msg)
        return False