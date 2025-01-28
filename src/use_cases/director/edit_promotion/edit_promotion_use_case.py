from repositories.promotion_repository import PromotionRepository
from fastapi import Request, Response
from entities.promotion import Promotion
from use_cases.director.edit_promotion.edit_promotion_dto import EditPromotionDTO

class EditPromotionUseCase:
    def __init__(self, promotion_repository: PromotionRepository):
        self.promotion_repository = promotion_repository

    def execute(self, promotion_id: str, edit_promotion_dto: EditPromotionDTO, response: Response, request: Request):
        try:
            self.promotion_repository.update(promotion_id, edit_promotion_dto)
            
            response.status_code = 200
            return {"status": "success", "message": "Promoção atualizada com sucesso"}       
        except ValueError as e:
            response.status_code = 404
            return {"status": "error", "message": str(e)}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": "Erro ao atualizar a promoção"}
