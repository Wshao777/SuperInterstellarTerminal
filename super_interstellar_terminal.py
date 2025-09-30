import asyncio
from datetime import datetime
import os
import sys

# --- 1. 整合金流通知模組 ---
# 確保 bank_notify.py 中的所有函式都可以直接被這個腳本調用
# 這裡將您提供的 bank_notify.py 內容簡化並整合，以直接調用 verify_bank_transfer

# 假設這裡已經包含了您提供的 bank_notify.py 中的所有函式和設定
# 為了讓這個單一腳本可執行，我們直接將核心邏輯包含進來
import requests

# 從 .env 讀取設定（模擬）
# 註：在真實環境中，Flask/Pydroid3 會自動載入。這裡為確保單腳本執行，我們直接使用 os.getenv。
BANK_CTBC_CODE = os.getenv("BANK_CTBC_CODE", "822")
BANK_CTBC_ACCOUNT = os.getenv("BANK_CTBC_ACCOUNT", "484540302460")
BANK_POST_CODE = os.getenv("BANK_POST_CODE", "700")
BANK_POST_ACCOUNT = os.getenv("BANK_POST_ACCOUNT", "00210091602429")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_DEFAULT_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "YOUR_DEFAULT_CHAT_ID")

def send_telegram_notify(message: str):
    """將交易/金流結果推送到 Telegram"""
    if TELEGRAM_TOKEN == "YOUR_DEFAULT_BOT_TOKEN" or TELEGRAM_CHAT_ID == "YOUR_DEFAULT_CHAT_ID":
        print(f"⚠️ Telegram 未設定，請配置 .env：{message}")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        response = requests.post(url, data=data, timeout=5)
        if response.status_code == 200:
            print("✅ Telegram 通知送出成功")
        else:
            print(f"❌ Telegram 錯誤：{response.text}")
    except Exception as e:
        print(f"❌ Telegram 連線失敗：{e}")

def verify_bank_transfer(bank_code, account, amount, from_bank="自動化派單系統"):
    """模擬金流入帳驗證並發出 Telegram 通知"""
    banks = {
        BANK_CTBC_CODE: f"中信 {BANK_CTBC_ACCOUNT}",
        BANK_POST_CODE: f"郵政 {BANK_POST_ACCOUNT}"
    }

    # 這裡直接模擬驗證成功，並發送 Telegram 通知
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if bank_code in banks:
        target_bank_info = banks[bank_code]
    else:
        target_bank_info = f"未知銀行 {bank_code}"

    msg = f"⚡ <b>HFT 派單資金結算入帳</b>\n" \
          f"🏦 入帳：{target_bank_info}\n" \
          f"💰 金額：{amount:,} NT$\n" \
          f"📅 時間：{now}\n" \
          f"🔗 來源：{from_bank}\n\n" \
          f"🛡️ 總司令，資金到位！帝國戰力 +{amount} 💜"
    send_telegram_notify(msg)
    return True

# --- 2. 升級 ThorHammerClient 以接收 SL/TP ---

class ThorHammerClient:
    """模擬 Thor's Hammer (pandora_core) 的客戶端介面"""
    def send_order(self, asset, action, quantity, stop_loss=None, take_profit=None):
        print(f"\n[🚀 STAR-TERMINAL >> THOR'S HAMMER] 指令派發")
        print(f"    > 交易: {action} {quantity} of {asset}")
        print(f"    > 止損 (SL): {stop_loss if stop_loss else '未設定'}")
        print(f"    > 止盈 (TP): {take_profit if take_profit else '未設定'}")

        # 這裡是真正的 Alpaca API 呼叫 (模擬成功)
        if stop_loss or take_profit:
            print("    > 🛡️ 訂單已建立 OCO (一取消一觸發) 保護機制。")

        # --- 自動化派單與金流驗證 (Auto APL & Bank Notify) ---
        # 假設每次成功的 HFT 派單都會觸發一筆模擬的金流入帳
        simulated_profit = int(quantity * 50) # 模擬每單位獲利 50 NTD

        # 假設所有資金都自動轉入中信帳戶
        verify_bank_transfer(BANK_CTBC_CODE, BANK_CTBC_ACCOUNT, simulated_profit)

        return {"status": "SUCCESS", "tx_id": f"TX-{datetime.now().timestamp()}", "profit": simulated_profit}

# --- 3. 升級 SuperInterstellarTerminal 以解析進階參數 ---

class SuperInterstellarTerminal:
    def __init__(self):
        self.hammer = ThorHammerClient()
        self.market_alerts = asyncio.Queue()
        self.running = True

    # 保持 _simulate_realtime_alerts 和 _display_alerts 不變

    async def _simulate_realtime_alerts(self):
        """模擬來自 '紫色女神核心' 的實時風險警報 (Grok/Volatility/Bid-Ask)"""
        # ... (保持原來的模擬警報邏輯，這裡省略以保持簡潔)
        await asyncio.sleep(2)
        alerts = [
            ("TSLA", "RISK_ALERT", "波動率突破 5.0% - 建議暫停買入。", "HIGH"),
            ("BTC", "MARKET_OPPORTUNITY", "Grok 4 偵測到'Mooning'趨勢，情緒分數達 1.8。", "LOW"),
            ("AAPL", "LIQUIDITY_WARNING", "Bid-Ask 比例異常 (0.75) - 交易被系統中止。", "HIGH")
        ]

        for asset, type, msg, severity in alerts:
            alert_msg = f"[{datetime.now().strftime('%H:%M:%S')}] [ALERT: {type}][{severity}] {asset}: {msg}"
            await self.market_alerts.put(alert_msg)
            await asyncio.sleep(3)

    async def _display_alerts(self):
        """實時顯示從 '紫色女神核心' 接收到的警報"""
        while self.running:
            try:
                alert = await asyncio.wait_for(self.market_alerts.get(), timeout=1.0)
                print(f"\n[🚨 TERMINAL ALERT] {alert}")
            except asyncio.TimeoutError:
                pass
            await asyncio.sleep(0.1)

    async def _handle_user_input(self):
        """處理用戶手動輸入的 '星際命令'"""
        print("\n\n--- 歡迎來到 SUPER INTERSTELLAR TERMINAL (S.I.T.) ---")
        print("可用命令:")
        print("    BUY/SELL <資產> <數量> [--sl <止損價>] [--tp <止盈價>]")
        print("    STATUS, HELP, EXIT")

        while self.running:
            try:
                loop = asyncio.get_event_loop()
                command = await loop.run_in_executor(None, input, "\nS.I.T. Command > ")

                parts = command.split()
                if not parts:
                    continue

                cmd = parts[0].upper()

                if cmd == "EXIT":
                    self.running = False
                    break
                elif cmd == "STATUS":
                    print("[S.I.T. STATUS] 系統運行中，等待實時數據與命令...")
                elif cmd == "HELP":
                    print("\n--- S.I.T. HELP ---")
                    print("BUY/SELL <ASSET> <QTY> [--sl <PRICE>] [--tp <PRICE>]")
                    print("  Example 1: BUY BTC 10 --sl 60000 --tp 75000")
                    print("  Example 2: SELL TSLA 500")
                    print("  --sl: Stop Loss (止損價), 必須為數字")
                    print("  --tp: Take Profit (止盈價), 必須為數字")
                elif cmd in ["BUY", "SELL"]:
                    if len(parts) < 3:
                        print("錯誤: 交易指令格式不正確。應為: BUY/SELL <資產> <數量> [--sl <價格>] [--tp <價格>]")
                        continue

                    try:
                        action = cmd
                        asset = parts[1]
                        quantity = int(parts[2])
                        stop_loss = None
                        take_profit = None

                        # 迭代解析可選參數
                        i = 3
                        while i < len(parts):
                            if parts[i].lower() == '--sl' and i + 1 < len(parts):
                                stop_loss = float(parts[i+1])
                                i += 2
                            elif parts[i].lower() == '--tp' and i + 1 < len(parts):
                                take_profit = float(parts[i+1])
                                i += 2
                            else:
                                print(f"錯誤: 未知的參數 '{parts[i]}'")
                                # Break to avoid infinite loops on bad input
                                break

                        # 派發命令
                        result = self.hammer.send_order(asset, action, quantity, stop_loss, take_profit)
                        print(f"[S.I.T. RESPONSE] Order Result: {result}")
                        print(f"    > 💵 成功模擬金流自動入帳 (APL): {result['profit']:,} NT$！")

                    except ValueError:
                        print("錯誤: 數量、止損或止盈價格必須是有效的數字。")
                    except Exception as e:
                        print(f"指令處理時發生意外錯誤: {e}")

                else:
                    print("未知命令。請輸入 HELP 或 EXIT。")

            except EOFError:
                self.running = False
            except Exception as e:
                print(f"命令處理錯誤: {e}")

    async def run(self):
        """啟動終端機的主要異步任務"""
        # 協程並發運行
        await asyncio.gather(
            self._simulate_realtime_alerts(),
            self._handle_user_input(),
            self._display_alerts()
        )

# 執行主程序
if __name__ == "__main__":
    # 在 Windows 上需要特定的策略，這裡做一個兼容性檢查
    if sys.platform == "win32":
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except AttributeError:
            pass # 某些舊版 Python 沒有這個屬性

    terminal = SuperInterstellarTerminal()
    try:
        asyncio.run(terminal.run())
    except KeyboardInterrupt:
        print("\n\n[S.I.T. Shutdown] 星際終端已關閉。")