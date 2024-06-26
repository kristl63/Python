from dotenv import load_dotenv
import os
load_dotenv()
# INPUT YOUR API KEYS, TRADING SYMBOL AND CANDLE LENGHT, ALL IN UPPERCASE

# INPUT:
API_KEY = str(os.getenv("API_KEY"))
API_SECRET = str(os.getenv("API_SECRET"))
SYMBOL = 'BTCUSDT'
CANDLES = "1M"
RSI_OVER = 70
RSI_UNDER = 30
TRADE_QUANTITY = 0.01
RSI_PERIOD = 14  # NUBER OF SPACES BETWEEN CANDLES TO COUNT FROM
ORDER_TYPE = "MARKET"


# NO TOUCHING ZONE
SYMBOL = SYMBOL.lower()
WSS_BASE = "wss://stream.binancefuture.com/ws/"
KLINE = "@kline_"
CANDLES = CANDLES.lower()
FINAL_WSS = WSS_BASE+SYMBOL+KLINE+CANDLES

# print(FINAL_WSS)
# "wss://stream.binancefuture.com/ws/btcusdt@kline_1m"
