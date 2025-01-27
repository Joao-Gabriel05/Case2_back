from repositories.plan_respository import PlanRepository
from .delete_plan_use_case import DeletePlanByIDUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()
delete_plan_use_case = DeletePlanByIDUseCase(PlanRepository())
@router.delete("/director/delete-plan/{plan_id}")
def delete_plan(plan_id:str,response:Response, request:Request):
    return delete_plan_use_case.execute(plan_id,response, request)
