from repositories.client_repository import ClientsRepository
from fastapi import Request, Response
import jwt
import os

class GetClientDataUseCase:
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

        # Se não encontrar o usuário
        if not client_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        try:
            # Buscando os dados do cliente usando o client_id
            phone = self.client_repository.get_phone(client_id)
            city = self.client_repository.get_city(client_id)
            cep = self.client_repository.get_cep(client_id)
            street_number = self.client_repository.get_street_number(client_id)
            cart = self.client_repository.get_cart(client_id)
            # Verifica se algum dado não foi encontrado
            if not any([phone, city, cep, street_number,cart]):
                response.status_code = 404
                return {"status": "error", "message": "Cliente não encontrado ou dados ausentes"}

            # Retorna os dados do cliente
            response.status_code = 200
            return {
                "status": "success",
                "message": "Dados do cliente encontrados",
                "client_data": {
                    "phone": phone,
                    "city": city,
                    "cep": cep,
                    "street_number": street_number,
                    "cart": cart
                }
            }

        except Exception as e:
            # Caso ocorra algum erro inesperado
            response.status_code = 500
            return {"status": "error", "message": str(e)}
