from repositories.plan_respository import PlanRepository
from fastapi import Request, Response
from entities.plan import Plan

class GetPlanByIDUseCase:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    def execute(self, plan_id: str, response: Response, request: Request):

        plan = self.plan_repository.get_plan_by_id(plan_id)
        if not plan:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return plan