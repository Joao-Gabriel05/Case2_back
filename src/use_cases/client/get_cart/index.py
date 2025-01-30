from repositories.client_repository import ClientsRepository
from .get_cart_use_case import GetClientCartUseCase
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_client_auth_token import validade_client_auth_token

router = APIRouter()

# Instanciando o caso de uso
get_cart_use_case = GetClientCartUseCase(ClientsRepository())

@router.get("/client/cart", dependencies=[Depends(validade_client_auth_token)])
def cart_client( response: Response, request: Request):
    """
    Atualiza os dados do cliente usando o token do cliente extraído dos cookies para identificar o cliente.
    """
    # Executar o caso de uso para editar os dados
    return get_cart_use_case.execute( response, request)
