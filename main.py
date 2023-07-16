import uvicorn

from logging import getLogger
from logging import config

from modules.api.app import create_app
from modules.api.routes import init_api_routes

from config import AppServerConfig

config.fileConfig("config/logging.cfg")

server_config = AppServerConfig()

app = create_app()
init_api_routes(app)

def main() -> None:
    uvicorn.run("main:app", **server_config.dict())

if __name__ == "__main__":
    main()
