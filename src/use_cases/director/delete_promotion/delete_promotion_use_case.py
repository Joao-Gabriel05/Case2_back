from repositories.promotion_repository import PromotionRepository
from fastapi import Request, Response
from entities.promotion import Promotion

class DeletePromotionByIDUseCase:
    def __init__(self, promotion_repository: PromotionRepository):
        self.promotion_repository = promotion_repository

    def execute(self, promotion_id: str, response: Response, request: Request):

        plan = self.promotion_repository.delete_promotion(promotion_id)
        if not plan:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return {"status": "success", "message": "Promoção excluida"}