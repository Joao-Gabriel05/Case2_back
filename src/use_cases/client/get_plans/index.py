from repositories.plan_respository import PlanRepository
from .get_plan_use_case import GetPlanUseCase
from .get_plan_by_id_use_case import GetPlanByIDUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_plan_use_case = GetPlanUseCase(PlanRepository())
get_plan_by_id_use_case = GetPlanByIDUseCase(PlanRepository())

@router.get("/director/get-plan")
def get_plan( response:Response, request:Request):
    return get_plan_use_case.execute(response, request)

@router.get("/director/get-plan/{plan_id}")
def get_plan_by_id(plan_id: str ,response:Response, request:Request):
    return get_plan_by_id_use_case.execute(plan_id,response, request)