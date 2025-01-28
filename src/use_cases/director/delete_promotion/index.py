from repositories.promotion_repository import PromotionRepository
from .delete_promotion_use_case import DeletePromotionByIDUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()
delete_promotion_use_case = DeletePromotionByIDUseCase(PromotionRepository())
@router.delete("/director/delete-promotion/{promotion_id}")
def delete_promotion(promotion_id:str,response:Response, request:Request):
    return delete_promotion_use_case.execute(promotion_id,response, request)
