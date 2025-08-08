import yfinance as yf
from typing import Optional, Dict

def fetch_comparison_stats(ticker1: str, ticker2: str, start: Optional[str], end: Optional[str]) -> Dict:
    def get_stats(ticker):
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            return None
        return {
            "high": round(data["High"][ticker].max(), 2),
            "low": round(data["Low"][ticker].min(), 2),
            "average": round(data["Close"][ticker].mean(), 2),
            "last_close": round(data["Close"][ticker].iloc[-1], 2)
        }

    stats1 = get_stats(ticker1)
    stats2 = get_stats(ticker2)

    return {
        ticker1.upper(): stats1 or {"error": "No data found"},
        ticker2.upper(): stats2 or {"error": "No data found"}
    }
