import yfinance as yf
from typing import Optional

def get_latest_price(ticker: str) -> Optional[dict]:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")  # get last 2 trading days
        if hist.empty or len(hist) < 2:
            return None

        prev_close = hist['Close'].iloc[-2]
        last_close = hist['Close'].iloc[-1]
        change = round(last_close - prev_close, 2)
        change_percent = round((change / prev_close) * 100, 2)

        return {
            "ticker": ticker.upper(),
            "previous_close": round(prev_close, 2),
            "last_close": round(last_close, 2),
            "change": change,
            "change_percent": change_percent
        }
    except:
        return None
