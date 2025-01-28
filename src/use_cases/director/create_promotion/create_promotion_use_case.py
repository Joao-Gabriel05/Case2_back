from repositories.promotion_repository import PromotionRepository  # Substitua com o repositório de promoções
from use_cases.director.create_promotion.create_promotion_dto import CreatePromotionDTO  # DTO para promoção
from fastapi import Request, Response
from entities.promotion import Promotion  # Entidade de Promoção

class CreatePromotionUseCase:
    def __init__(self, promotion_repository: PromotionRepository):
        self.promotion_repository = promotion_repository

    def execute(self, create_promotion_dto: CreatePromotionDTO, response: Response, request: Request):
        # Verificar se todos os campos obrigatórios foram preenchidos
        if (not create_promotion_dto.description or 
            not create_promotion_dto.plan or 
            not create_promotion_dto.price):
            response.status_code = 407
            return {"status": "error", "message": "Faltam informações"}

        # Criar a instância da promoção
        promotion = Promotion(
            description=create_promotion_dto.description,
            plan=create_promotion_dto.plan,
            price=create_promotion_dto.price
        )

        # Salvar a promoção no repositório
        self.promotion_repository.save(promotion)
        
        # Retornar resposta de sucesso
        response.status_code = 201
        return {"status": "success", "message": "Promoção criada"}
