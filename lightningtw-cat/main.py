import argparse
import os
import pandas as pd
import telegram
from dotenv import load_dotenv

def dispatch_orders():
    """Placeholder function for dispatching orders."""
    print("😼⚡️ AI 派單系統啟動中...")
    # TODO: Add logic to receive and dispatch orders.
    print("✅ 派單任務完成。")

def generate_report():
    """
    Reads order data from a CSV, calculates a summary, and sends it to Telegram.
    """
    print("📊 正在生成報表...")
    try:
        df = pd.read_csv('dummy_orders.csv')

        # Calculate metrics
        completed_orders = df[df['status'] == 'completed']
        total_orders = len(df)
        completed_count = len(completed_orders)
        total_revenue = completed_orders['revenue'].sum()

        # Format the report message
        report_message = (
            f"📊 **小閃電貓每日戰報** ⚡\n\n"
            f"總訂單數：{total_orders}\n"
            f"完成訂單數：{completed_count}\n"
            f"總收益：${total_revenue:,.2f} 💰\n\n"
            f"幹得不錯，總司令！😼"
        )

        print("報表內容：\n" + report_message)

        # Send to Telegram
        token = os.getenv("TELEGRAM_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT")
        bot = telegram.Bot(token=token)
        bot.send_message(chat_id=chat_id, text=report_message, parse_mode='Markdown')

        print(f"✅ 報表已成功發送至 Telegram Chat ID: {chat_id}。")

    except FileNotFoundError:
        print("❌ 錯誤：找不到 `dummy_orders.csv` 檔案。")
    except Exception as e:
        print(f"❌ 產生報表時發生未知錯誤：{e}")


def check_cash_flow():
    """Placeholder function for checking cash flow."""
    print("💰 正在檢查金流...")
    # TODO: Add logic to monitor payments and detect anomalies.
    print("✅ 金流檢查完成，無異常。")

def simulate_strategy():
    """Placeholder function for simulating strategies."""
    print("💎 正在進行策略模擬...")
    # TODO: Add logic for simulating dispatch strategies and calculating ROI.
    print("✅ 策略模擬完成。")

def main():
    """Main function to parse arguments and run tasks."""
    # Load environment variables from .env file
    load_dotenv()

    # Check for required environment variables
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    telegram_chat = os.getenv("TELEGRAM_CHAT")
    api_key = os.getenv("API_KEY")

    if not all([telegram_token, telegram_chat, api_key]):
        print("❌ 錯誤：必要的環境變數（TELEGRAM_TOKEN, TELEGRAM_CHAT, API_KEY）尚未在 .env 檔案中設定。")
        print("請複製 .env.example 並填寫您的金鑰。")
        return

    parser = argparse.ArgumentParser(description="小閃電貓⚡ AI 雷霆助理")
    parser.add_argument("--派單", action="store_true", help="自動派送今日訂單")
    parser.add_argument("--報表", action="store_true", help="生成報表並發送 Telegram")
    parser.add_argument("--金流檢查", action="store_true", help="監控金流異常")
    parser.add_argument("--策略模擬", action="store_true", help="模擬不同派單策略並輸出結果")

    args = parser.parse_args()

    print("--- ⚡ 小閃電貓任務啟動 ⚡ ---")
    if args.派單:
        dispatch_orders()
    elif args.報表:
        generate_report()
    elif args.金流檢查:
        check_cash_flow()
    elif args.策略模擬:
        simulate_strategy()
    else:
        print("🤔 請提供一個操作指令，例如：--派單")
        parser.print_help()
    print("--- 任務結束 ---")


if __name__ == "__main__":
    main()
