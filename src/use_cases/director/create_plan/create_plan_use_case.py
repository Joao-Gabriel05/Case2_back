from repositories.plan_respository import PlanRepository  # Substitua com o repositório de planos
from use_cases.director.create_plan.create_plan_dto import CreatePlanDTO  # DTO para o plano
from fastapi import Request, Response
from entities.plan import Plan  # Entidade de Plano

class CreatePlanUseCase:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    def execute(self, create_plan_dto: CreatePlanDTO, response: Response, request: Request):
        # Verificar se todos os campos obrigatórios foram preenchidos
        if (not create_plan_dto.type or 
            not create_plan_dto.speed or 
            not create_plan_dto.details or
            not create_plan_dto.price or
            not create_plan_dto.public):
            response.status_code = 407
            return {"status": "error", "message": "faltam informações"}

        # Criar a instância do plano
        plan = Plan(
            type=create_plan_dto.type,
            speed=create_plan_dto.speed,
            details=create_plan_dto.details,
            price = create_plan_dto.price,
            public = create_plan_dto.public
        )

        # Salvar o plano no repositório
        self.plan_repository.save(plan)
        
        # Retornar resposta de sucesso
        response.status_code = 201
        return {"status": "success", "message": "Plano criado"}
