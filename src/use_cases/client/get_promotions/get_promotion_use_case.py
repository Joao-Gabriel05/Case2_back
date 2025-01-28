from repositories.promotion_repository import PromotionRepository
from fastapi import Request, Response

class GetPromotionUseCase:
    def __init__(self, promotion_repository: PromotionRepository):
        self. promotion_repository =  promotion_repository

    def execute(self, response: Response, request: Request):

        promotions = self. promotion_repository.get_all_promotions()
        if not promotions:
            response.status_code = 204
            return {"status": "success", "message": "Nenhuma promoção encontrada"}
        
        response.status_code = 200
        return promotions