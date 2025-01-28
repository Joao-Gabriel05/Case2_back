from repositories.promotion_repository import PromotionRepository
from .create_promotion_dto import CreatePromotionDTO
from .create_promotion_use_case import CreatePromotionUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_promotion_use_case = CreatePromotionUseCase(PromotionRepository())

@router.post("/director/create-promotion")
def create_promotion(create_promotion_dto:CreatePromotionDTO, response:Response, request:Request):
    return create_promotion_use_case.execute(create_promotion_dto, response, request)

