from repositories.promotion_repository import PromotionRepository
from .edit_promotion_dto import EditPromotionDTO
from .edit_promotion_use_case import EditPromotionUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

edit_promotion_use_case = EditPromotionUseCase(PromotionRepository())
@router.put("/director/edit-promotion/{promotion_id}")
def edit_promotion(promotion_id: str, edit_promotion_dto: EditPromotionDTO, response: Response, request: Request):
    return edit_promotion_use_case.execute(promotion_id, edit_promotion_dto, response, request)