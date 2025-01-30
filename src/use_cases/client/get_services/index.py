from fastapi import APIRouter, Request, Response, Depends
from repositories.client_repository import ClientsRepository
from use_cases.client.get_services.get_services_use_case import GetClientServiceUseCase
from middlewares.validate_client_auth_token import validade_client_auth_token

router = APIRouter()

# Instanciando o caso de uso
get_client_services_use_case = GetClientServiceUseCase(ClientsRepository())

@router.get("/client/services", dependencies=[Depends(validade_client_auth_token)])
async def get_client_services( response: Response, request: Request):
    return get_client_services_use_case.execute( response, request)
