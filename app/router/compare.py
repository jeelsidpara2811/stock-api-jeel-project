from fastapi import APIRouter, HTTPException
from typing import Optional
from app.services.compare_services import fetch_comparison_stats

router = APIRouter()

@router.get("/api/compare")
def compare_stocks(
    ticker1: str,
    ticker2: str,
    start: Optional[str] = None,
    end: Optional[str] = None
):
    result = fetch_comparison_stats(ticker1, ticker2, start, end)

    if "error" in result.get(ticker1.upper(), {}) and "error" in result.get(ticker2.upper(), {}):
        raise HTTPException(status_code=404, detail="No data found for either ticker")

    return result
