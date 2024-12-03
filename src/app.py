from fastapi import FastAPI

from src.api.tariff import router as tariff_router


app = FastAPI(
    title="SMIT API",
    description="API for managing tariffs and calculating costs.",
    version="1.0.0",
)


app.include_router(tariff_router)
