import yfinance as yf
from functools import lru_cache
from typing import Optional, Dict

# Data caching for performance and to avoid repeated downloads
@lru_cache(maxsize=100)

# Function to fetch comparison statistics for two stocks
def fetch_comparison_stats(ticker1: str, ticker2: str, start: Optional[str], end: Optional[str]) -> Dict:
    def get_stats(ticker):
        hist = yf.Ticker(ticker).history(start=start, end=end, auto_adjust=False)
        if hist.empty:
            return None
        result = {
            "high": round(hist["High"].max(), 2),
            "low": round(hist["Low"].min(), 2),
            "average": round(hist["Close"].mean(), 2),
            "last_close": round(hist["Close"].iloc[-1], 2),
        }
        
        # Only include these when BOTH start and end are omitted
        if not start and not end:
            result["start_date"] = str(hist.index[0].date())
            result["end_date"] = str(hist.index[-1].date())

        return result
    
# Fetch statistics for both tickers
    stats1 = get_stats(ticker1)
    stats2 = get_stats(ticker2)
    
# If both tickers return None, return an error message
    return {
        ticker1.upper(): stats1 or {"error": "No data found"},
        ticker2.upper(): stats2 or {"error": "No data found"}
    }
