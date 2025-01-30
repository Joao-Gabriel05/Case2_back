from repositories.client_repository import ClientsRepository
from fastapi import Request, Response
import jwt
import os

class GetClientCartUseCase:
    def __init__(self, client_repository: ClientsRepository):
        self.client_repository = client_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("client_auth_token")
        try:
            # Verifica o token JWT
            payload = jwt.decode(token.split(" ")[1], os.getenv("CLIENT_JWT_SECRET"), algorithms=["HS256"])
            client_id = payload.get("id")
        except (jwt.DecodeError, IndexError, AttributeError):
            response.status_code = 401
            return {"status": "error", "message": "Invalid or missing token"}

        # Se não encontrar o cliente
        if not client_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        try:
            # Busca o cart do cliente
            client_cart = self.client_repository.get_cart(client_id)
            
            if client_cart is None:
                response.status_code = 404
                return {"status": "error", "message": "Carrinho não encontrado"}
            
            # Retorna o cart do cliente
            response.status_code = 200
            return {"status": "success", "cart": client_cart}

        except Exception as e:
            # Caso ocorra algum erro inesperado
            response.status_code = 500
            return {"status": "error", "message": "Erro ao obter os dados do carrinho"}
