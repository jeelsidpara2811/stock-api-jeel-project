from fastapi import APIRouter, HTTPException
from app.services.latest_services import get_latest_price

router = APIRouter()

@router.get("/api/latest")
def latest_price(ticker: str):
    result = get_latest_price(ticker)
    if result is None:
        raise HTTPException(status_code=404, detail="Unable to retrieve latest price")
    return result