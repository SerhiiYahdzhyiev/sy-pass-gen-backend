from fastapi import FastAPI

from .config import API_TITLE
from .config import API_DESCRIPTION
from .config import API_VERSION

def create_app() -> FastAPI:
    return FastAPI(
        title=API_TITLE,
        description=API_DESCRIPTION,
        version=API_VERSION
        )
