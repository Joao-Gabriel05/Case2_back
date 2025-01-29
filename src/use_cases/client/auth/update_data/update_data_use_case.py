from repositories.client_repository import ClientsRepository  # Supondo que você tenha esse repositório
from fastapi import Request, Response
from entities.client import Client  # Supondo que você tenha a entidade Client
from use_cases.client.auth.update_data.update_data_dto import UpdateClientDTO  # Seu DTO

class EditClientUseCase:
    def __init__(self, client_repository: ClientsRepository):
        self.client_repository = client_repository

    def execute(self, client_id: str, update_client_dto: UpdateClientDTO, response: Response, request: Request):
        try:
            # Converte o DTO para um dicionário
            update_data = update_client_dto.dict()

            # Atualiza os campos individualmente se eles estiverem presentes no DTO
            if 'phone' in update_client_dto:
                self.client_repository.update_phone(client_id, update_data['phone'])
            
            if 'city' in update_client_dto:
                self.client_repository.update_city(client_id, update_data['city'])
            
            if 'cep' in update_client_dto:
                self.client_repository.update_cep(client_id, update_data['cep'])
            
            if 'street_number' in update_client_dto:
                self.client_repository.update_street_number(client_id, update_data['street_number'])
            

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
