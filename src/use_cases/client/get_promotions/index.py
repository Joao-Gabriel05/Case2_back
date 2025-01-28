

from repositories.promotion_repository import PromotionRepository
from .get_promotion_use_case import GetPromotionUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_promotion_use_case = GetPromotionUseCase(PromotionRepository())

@router.get("/client/get-promotion")
def get_promotion( response:Response, request:Request):
    return get_promotion_use_case.execute(response, request)