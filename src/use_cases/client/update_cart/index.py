from repositories.client_repository import ClientsRepository
from .update_cart_dto import UpdateCartDTO
from .update_cart_use_case import EditCartUseCase
from fastapi import Request, Response, APIRouter, Depends
from middlewares.validate_client_auth_token import validade_client_auth_token

router = APIRouter()

# Instanciando o caso de uso
edit_cart_use_case = EditCartUseCase(ClientsRepository())

@router.put("/client/edit-cart", dependencies=[Depends(validade_client_auth_token)])
def edit_client(edit_client_dto: UpdateCartDTO, response: Response, request: Request):
    """
    Atualiza os dados do cliente usando o token do cliente extraído dos cookies para identificar o cliente.
    """
    # Executar o caso de uso para editar os dados
    return edit_cart_use_case.execute(edit_client_dto, response, request)
