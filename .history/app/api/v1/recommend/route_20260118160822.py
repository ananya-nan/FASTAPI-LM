from fastapi import APIRouter
from .schema import RecommendRequest
from .service import search_predict

router = APIRouter()

@router.post("/", tags=["Recommendations"])
def get_recommendations(data: RecommendRequest):
    return search_predict(
        query=data.query,
        top_k=data.top_k,
        type=data.type
    )
