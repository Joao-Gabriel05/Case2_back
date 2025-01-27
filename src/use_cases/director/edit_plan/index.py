from repositories.plan_respository import PlanRepository
from .edit_plan_dto import EditPlanDTO
from .edit_plan_use_case import EditPlanUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

edit_plan_use_case = EditPlanUseCase(PlanRepository())
@router.put("/director/edit-plan/{plan_id}")
def edit_plan(plan_id: str, edit_plan_dto: EditPlanDTO, response: Response, request: Request):
    return edit_plan_use_case.execute(plan_id, edit_plan_dto, response, request)