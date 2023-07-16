import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class AppServerConfig(BaseModel):
    host: str = os.environ.get("HOST") or "localhost"
    port: int = int(os.environ.get("PORT")) or 8000
    reload: bool = True if os.environ.get("MODE") == "development" else False
    log_config: str = "config/logging.cfg"
