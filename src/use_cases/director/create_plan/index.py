from repositories.plan_respository import PlanRepository
from .create_plan_dto import CreatePlanDTO
from .create_plan_use_case import CreatePlanUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_plan_use_case = CreatePlanUseCase(PlanRepository())

@router.post("/director/create-plan")
def create_plan(create_plan_dto:CreatePlanDTO, response:Response, request:Request):
    return create_plan_use_case.execute(create_plan_dto, response, request)

