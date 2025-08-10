from functools import lru_cache
import yfinance as yf
from typing import Optional, Dict

# Data caching for performance and to avoid repeated downloads
@lru_cache(maxsize=100)

# Function to fetcg stock statistics
def fetch_stock_stats(ticker: str, start: Optional[str], end: Optional[str]) -> Optional[Dict]:
    hist = yf.Ticker(ticker).history(start=start, end=end, auto_adjust=False)
    
    result = {
        "ticker": ticker.upper(),
        "high": round(hist["High"].max(), 2),
        "low": round(hist["Low"].min(), 2),
        "average": round(hist["Close"].mean(), 2),
        "last_close": round(hist["Close"].iloc[-1], 2),
    }

# If start and end dates are not provided, include them in the result
    if not start and not end:
        result["start_date"] = str(hist.index[0].date())
        result["end_date"] = str(hist.index[-1].date())

    return result