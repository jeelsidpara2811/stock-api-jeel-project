from fastapi import APIRouter, HTTPException
from typing import Optional
from app.services.compare_services import fetch_comparison_stats

# Create a instance 
router = APIRouter()

# Endpoint to compare two stocks
@router.get("/api/compare")

# Define the query parameters and optional date range
def compare_stocks(
    ticker1: str,
    ticker2: str,
    start: Optional[str] = None,
    end: Optional[str] = None
):
# Fetch comparison statistics for the 2 stocks and string formate for start and end is (YYYY-MM-DD)
    result = fetch_comparison_stats(ticker1, ticker2, start, end)

# If both sides shows error then it returns 404 or if one works, still returns 200 with one side having an error
    if "error" in result.get(ticker1.upper(), {}) and "error" in result.get(ticker2.upper(), {}):
        raise HTTPException(status_code=404, detail="No data found for either ticker")
    
# Return the result if it is not None
    return result
