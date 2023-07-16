from fastapi import status
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Body
from pydantic import BaseModel

from modules.generator import generate

router = APIRouter()

class ResponseModel(BaseModel):
    password_suggestion: str

class GeneratorParams(BaseModel):
    length: int = 12
    lowercase: bool = True
    uppercase: bool = True
    digits: bool = True
    special: bool = True

@router.post("/generate", response_model=ResponseModel)
def generate_password_sugestion(params: GeneratorParams):
    suggestion = ""
    try:
        suggestion = generate(**params.dict())
    except BaseException as e:
        raise HTTPException(
                status_code=500,
                detail=str(e)
            )
    return ResponseModel(password_suggestion=suggestion) 
