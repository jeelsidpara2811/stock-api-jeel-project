from fastapi import FastAPI
from app.router.stats import router as stats_router
from app.router.compare import router as compare_router

app = FastAPI()
app.include_router(stats_router)
app.include_router(compare_router)