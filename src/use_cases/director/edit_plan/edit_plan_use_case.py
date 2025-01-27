from repositories.plan_respository import PlanRepository
from fastapi import Request, Response
from entities.plan import Plan
from use_cases.director.edit_plan.edit_plan_dto import EditPlanDTO

class EditPlanUseCase:
    def __init__(self, plan_repository: PlanRepository):
        self.plan_repository = plan_repository

    def execute(self, plan_id: str, edit_plan_dto: EditPlanDTO, response: Response, request: Request):
        try:
            self.plan_repository.update(plan_id, edit_plan_dto)
            
            response.status_code = 200
            return {"status": "success", "message": "Plano atualizada com sucesso"}       
        except ValueError as e:
            response.status_code = 404
            return {"status": "error", "message": str(e)}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": "Erro ao atualizar o plano"}
