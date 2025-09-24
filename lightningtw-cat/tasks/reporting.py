import os
import pandas as pd
import telegram
import financial_services

def run_daily_report():
    """
    Generates the daily report and sends it to Telegram.
    """
    print("📊 正在生成報表...")
    report_bot_token = os.getenv("REPORT_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    try:
        df = pd.read_csv('dummy_orders.csv')
        completed_orders = df[df['status'] == 'completed']
        report_message = (
            f"📊 **小閃電貓每日戰報** ⚡\n\n"
            f"總訂單數：{len(df)}\n"
            f"完成訂單數：{len(completed_orders)}\n"
            f"總收益：${completed_orders['revenue'].sum():,.2f} 💰\n\n"
            f"幹得不錯，總司令！😼"
        )
        bot = telegram.Bot(token=report_bot_token)
        bot.send_message(chat_id=telegram_chat_id, text=report_message, parse_mode='Markdown')
        return {"status": "completed", "report": report_message}
    except Exception as e:
        print(f"❌ Error generating report: {e}")
        return {"status": "error", "message": str(e)}

def run_cash_flow_check():
    """
    Runs a simulation of the financial services module to check cash flow.
    """
    print("💰 正在啟動金流檢查...")
    financial_services.simulate_and_check_flow()
    return {"status": "completed", "message": "金流檢查模擬完成。所有通知與紀錄應已發送。"}
