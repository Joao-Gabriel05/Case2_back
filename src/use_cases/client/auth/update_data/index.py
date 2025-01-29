# from repositories.client_repository import ClientRepository
# from .update_data_dto import UpdateClientDTO
# from .update_data_use_case import EditClientUseCase
# from fastapi import Request, Response, APIRouter

# router = APIRouter()

# edit_client_use_case = EditClientUseCase(ClientRepository())
# @router.put("/client/edit-data/{client_id}")
# def edit_plan(plan_id: str, edit_plan_dto: EditPlanDTO, response: Response, request: Request):
#     return edit_plan_use_case.execute(plan_id, edit_plan_dto, response, request)