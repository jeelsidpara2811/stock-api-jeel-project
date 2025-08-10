import yfinance as yf
from typing import Optional
from functools import lru_cache

# Data caching for performance and to avoid repeated downloads
@lru_cache(maxsize=100)

# Function to get latest stock price and it change
def get_latest_price(ticker: str) -> Optional[dict]:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d", auto_adjust=False)  # get last 2 trading days 
        if hist.empty or len(hist) < 2:    # Guards against insufficient data (e.g., holidays or bad ticker).
            return None
        
# Extract the last two days closing prices.
        prev_close = hist['Close'].iloc[-2]
        last_close = hist['Close'].iloc[-1]
        
# Get the dates for the last two trading days.        
        prev_date = hist.index[-2].date().isoformat()
        last_date = hist.index[-1].date().isoformat()
        
# Compute absolute and percentage change.
        change = round(last_close - prev_close, 2)
        change_percent = round((change / prev_close) * 100, 2)

        return {
            "ticker": ticker.upper(),
            "previous_date": prev_date,
            "previous_close": round(prev_close, 2),
            "last_date": last_date,
            "last_close": round(last_close, 2),
            "change": change,
            "change_percent": change_percent
        }
    except:
        return None