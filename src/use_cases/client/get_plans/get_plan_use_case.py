from repositories.plan_respository import PlanRepository
from fastapi import Request, Response

class GetPlanUseCase:
    def __init__(self, plan_repository: PlanRepository):
        self. plan_repository =  plan_repository

    def execute(self, response: Response, request: Request):

        plans = self. plan_repository.get_all_plans()
        if not plans:
            response.status_code = 404
            return {"message": "Nenhum plano encontrada"}
        
        response.status_code = 200
        return plans