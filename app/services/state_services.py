from functools import lru_cache
import yfinance as yf
from typing import Optional, Dict

@lru_cache(maxsize=100)
def fetch_stock_stats(ticker: str, start: Optional[str], end: Optional[str]) -> Optional[Dict]:
    data = yf.download(ticker, start=start, end=end, auto_adjust=False)
    if data.empty:
        return None

    return {
        "ticker": ticker.upper(),
        "start_date": str(data.index[0].date()),
        "end_date": str(data.index[-1].date()),
        "high": round(data['High'][ticker].max(), 2),
        "low": round(data['Low'][ticker].min(), 2),
        "average": round(data['Close'][ticker].mean(), 2),
        "last_close": round(data['Close'][ticker].iloc[-1], 2)
    }