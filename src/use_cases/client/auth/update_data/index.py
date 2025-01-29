from repositories.client_repository import ClientsRepository
from .update_data_dto import UpdateClientDTO
from .update_data_use_case import EditClientUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

edit_client_use_case = EditClientUseCase(ClientsRepository())
@router.put("/client/auth/edit-data/{client_id}")
def edit_client(client_id: str, edit_client_dto: UpdateClientDTO, response: Response, request: Request):
    return edit_client_use_case.execute(client_id, edit_client_dto, response, request)