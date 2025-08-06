from fastapi import APIRouter, HTTPException
from typing import Optional
from app.services.stock_services import fetch_stock_stats

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome Stock Stats API. Use /api/stats to get stock data."}

@router.get("/api/stats")
def get_stock_stats(ticker: str, start: Optional[str] = None, end: Optional[str] = None):
    result = fetch_stock_stats(ticker, start, end)
    if result is None:
        raise HTTPException(status_code=404, detail="Please provide valid inputs for ticker")
    return result
