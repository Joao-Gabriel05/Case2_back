from repositories.client_repository import ClientsRepository
from fastapi import Request, Response
import jwt
import os
from use_cases.client.update_data.update_data_dto import UpdateClientDTO  # Seu DTO

class EditClientUseCase:
    def __init__(self, client_repository: ClientsRepository):
        self.client_repository = client_repository

    def execute(self, update_client_dto: UpdateClientDTO, response: Response, request: Request):
        token = request.cookies.get("client_auth_token")
        print(token)
        try:
            # Verifica o token JWT
            payload = jwt.decode(token.split(" ")[1], os.getenv("CLIENT_JWT_SECRET"), algorithms=["HS256"])
            print(payload)
            client_id = payload.get("id")
        except (jwt.DecodeError, IndexError, AttributeError):
            response.status_code = 401
            return {"status": "error", "message": "Invalid or missing token"}

        # Se não encontrar o cliente
        if not client_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        try:
            # Converte o DTO para um dicionário
            update_data = update_client_dto.dict()
            print(update_data)
            # Atualiza os campos individualmente se eles estiverem presentes no DTO
            if 'phone' in update_data:
                self.client_repository.update_phone(client_id, update_data['phone'])
            
            if 'city' in update_data:
                self.client_repository.update_city(client_id, update_data['city'])
            
            if 'cep' in update_data:
                self.client_repository.update_cep(client_id, update_data['cep'])
            
            if 'street_number' in update_data:
                self.client_repository.update_street_number(client_id, update_data['street_number'])
            
            if 'cart' in update_data:
                self.client_repository.update_cart(client_id, update_data['cart'])

            response.status_code = 200
            return {"status": "success", "message": "Cliente atualizado com sucesso"}

        except ValueError as e:
            # Caso não encontre o cliente ou haja algum erro com os dados
            response.status_code = 404
            return {"status": "error", "message": str(e)}

        except Exception as e:
            # Caso ocorra algum erro inesperado
            response.status_code = 500
            return {"status": "error", "message": "Erro ao atualizar os dados do cliente"}
