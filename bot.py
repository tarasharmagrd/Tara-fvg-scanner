import requests
from tradingview_ta import TA_Handler, Interval

# --- APNI DETAILS YAHAN DALO ---
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN" 
CHAT_ID = "YOUR_CHAT_ID"

# 12 CME Symbols
SYMBOLS = [
    "CME:6E1!", "CME:6B1!", "CME:6J1!", "CME:6A1!", "CME:6C1!", 
    "CME:6S1!", "CME:6N1!", "CME:DX1!", "COMEX:GC1!", "COMEX:SI1!", 
    "CME:BTC1!", "CME:ETH1!"
]

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)

def scan():
    for symbol in SYMBOLS:
        for tf in [Interval.INTERVAL_1_HOUR, Interval.INTERVAL_4_HOUR]:
            try:
                handler = TA_Handler(symbol=symbol, exchange="CME", screener="cfd", interval=tf)
                # FVG Logic aur Alert yahan trigger hoga
                print(f"Checking {symbol} {tf}...")
            except: continue

if __name__ == "__main__":
    scan()
