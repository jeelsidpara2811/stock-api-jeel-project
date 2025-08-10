from fastapi import APIRouter, HTTPException
from typing import Optional
from app.services.stats_services import fetch_stock_stats

# Create a instance 
router = APIRouter()

@router.get("/")
# Root endpoint to provide a welcome message
def read_root():
    return {
        "MESSAGE": ("Welcome to the Stock Statistics API. Use Swagger UI or URL query parameter to explore the endpoints."),
        }

@router.get("/api/stats")
# Endpoint to get stock statistics and string formate for start and end is (YYYY-MM-DD)
def get_stock_stats(ticker: str, start: Optional[str] = None, end: Optional[str] = None):
    result = fetch_stock_stats(ticker, start, end)
    
# Check if the result is None and raise an HTTPException
    if result is None:
        raise HTTPException(status_code=404, detail="Please provide valid inputs for ticker")
    
# Return the result if it is not None
    return result
