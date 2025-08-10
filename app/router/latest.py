from fastapi import APIRouter, HTTPException
from app.services.latest_services import get_latest_price

# Creat a Instance of APIRouter
router = APIRouter()

# Define the endpoint 
@router.get("/api/latest")

# Define the query parameter 
def latest_price(ticker: str):
    result = get_latest_price(ticker)
    
# Check if the result is None and raise an HTTPException 
    if result is None:
        raise HTTPException(status_code=404, detail="Unable to retrieve latest price")
    
# Return the result if it is not None
    return result