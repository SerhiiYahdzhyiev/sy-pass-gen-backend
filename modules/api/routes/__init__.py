from fastapi import FastAPI

from .root import router as root_router
from .generator import router as generator_router

def init_api_routes(app: FastAPI) -> None:
    app.include_router(root_router, tags=["Root"])
    app.include_router(generator_router, tags=["Generator"])
