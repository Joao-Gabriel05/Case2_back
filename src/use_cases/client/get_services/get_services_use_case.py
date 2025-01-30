from repositories.client_repository import ClientsRepository
from fastapi import Request, Response
import jwt
import os

class GetClientServiceUseCase:
    def __init__(self, client_repository: ClientsRepository):
        self.client_repository = client_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("client_auth_token")
        print(token)
        try:
            # Verifica o token JWT
            payload = jwt.decode(token.split(" ")[1], os.getenv("CLIENT_JWT_SECRET"), algorithms=["HS256"])
            client_id = payload.get("id")
        except (jwt.DecodeError, IndexError, AttributeError):
            response.status_code = 401
            return {"status": "error", "message": "Invalid or missing token"}

        # Se não encontrar o usuário
        if not client_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        try:
            # Buscando o campo 'services' do cliente usando o client_id
            services = self.client_repository.get_services(client_id)

            # Verifica se os dados de serviços não foram encontrados
            if not services:
                response.status_code = 404
                return {"status": "error", "message": "Cliente não encontrado ou dados de serviços ausentes"}

            # Retorna os dados do cliente com os serviços
            response.status_code = 200
            return {
                "status": "success",
                "message": "Dados do cliente encontrados",
                "client_data": {
                    "services": services
                }
            }

        except Exception as e:
            # Caso ocorra algum erro inesperado
            response.status_code = 500
            return {"status": "error", "message": str(e)}
