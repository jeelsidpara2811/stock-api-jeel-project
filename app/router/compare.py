from fastapi import APIRouter

router = APIRouter()

@router.get("/api/compare")
def get_stock_msg():
    return {"message": "This endpoint is under construction. Please check back later."}