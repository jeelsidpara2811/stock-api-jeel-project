from fastapi import APIRouter, HTTPException
from typing import Optional
from app.services.state_services import fetch_stock_stats

router = APIRouter()

@router.get("/")
def read_root():
    return {"MESSAGE" : "Welcome to the stock statistics analysis through API. Use /docs in URL for stock Analysis via Swagger UI."}

@router.get("/api/stats")
def get_stock_stats(ticker: str, start: Optional[str] = None, end: Optional[str] = None):
    result = fetch_stock_stats(ticker, start, end)
    if result is None:
        raise HTTPException(status_code=404, detail="Please provide valid inputs for ticker")
    return result
