from fastapi import APIRouter, Request, Response, Depends
from repositories.client_repository import ClientsRepository
from use_cases.client.get_adress_info.get_adress_info_use_case import GetClientDataUseCase
from middlewares.validate_client_auth_token import validade_client_auth_token

router = APIRouter()

# Instanciando o caso de uso
get_client_data_use_case = GetClientDataUseCase(ClientsRepository())

@router.get("/client/adress", dependencies=[Depends(validade_client_auth_token)])
async def get_client_data( response: Response, request: Request):
    return get_client_data_use_case.execute( response, request)
