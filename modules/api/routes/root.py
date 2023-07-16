from fastapi import APIRouter
from fastapi import status
from pydantic import BaseModel

router = APIRouter()

class TestResponse(BaseModel):
  message: str = "Hello Password Generator!"


@router.get("/", tags=["Root"], status_code=status.HTTP_200_OK, response_model=TestResponse, description="Say hello.")
def say_hello():
  return TestResponse()
