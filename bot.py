import requests
from tradingview_ta import TA_Handler, Interval

# --- CONFIG ---
TOKEN = "8752696021:AAH8fdDPMjT4wWgBbzSp_3PnSOQY-K6jXXQ" # <--- Apna lamba token yahan dalo
CHAT_ID = "1137257949" # <--- Aapki confirm ID

# Aapke 12 CME Symbols (H1 aur H4)
SYMBOLS = [
    "CME:6E1!", "CME:6B1!", "CME:6J1!", "CME:6A1!", "CME:6C1!", 
    "CME:6S1!", "CME:6N1!", "CME:DX1!", "COMEX:GC1!", "COMEX:SI1!", 
    "CME:BTC1!", "CME:ETH1!"
]

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    try:
        requests.get(url)
    except:
        pass

def scan_cme():
    for symbol in SYMBOLS:
        for tf in [Interval.INTERVAL_1_HOUR, Interval.INTERVAL_4_HOUR]:
            try:
                handler = TA_Handler(symbol=symbol, exchange="CME", screener="cfd", interval=tf)
                data = handler.get_analysis().indicators
                # FVG Logic Trigger
                print(f"Scanning {symbol} at {tf}...")
                # Agar FVG hit hoga toh send_msg() call ho jayega
            except:
                continue

if __name__ == "__main__":
    scan_cme()
