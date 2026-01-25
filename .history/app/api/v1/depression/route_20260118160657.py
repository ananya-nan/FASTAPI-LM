from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest

router = APIRouter()

@router.post("/", tags=["Depression"])
def assess_depression(data: DepressionRequest):
    result = get_depression(data)
    return result

@router.get("/healthcheck", tags=["Depression"])
def health_check():
    return {"status": "ok"}
