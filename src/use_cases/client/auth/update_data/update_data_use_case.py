from repositories.client_repository import ClientRepository  # Supondo que você tenha esse repositório
from fastapi import Request, Response
from entities.client import Client  # Supondo que você tenha a entidade Client
from use_cases.client.auth.update_data.update_data_dto import UpdateClientDTO  # Seu DTO

class EditClientUseCase:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def execute(self, client_id: str, update_client_dto: UpdateClientDTO, response: Response, request: Request):
        try:
            # Supondo que o método update do repositório faz a atualização dos dados
            client = self.client_repository.update(client_id, update_client_dto)
            
            response.status_code = 200
            return {"status": "success", "message": "Cliente atualizado com sucesso", "client": client}
        
        except ValueError as e:
            # Caso não encontre o cliente ou haja algum erro com os dados
            response.status_code = 404
            return {"status": "error", "message": str(e)}
        
        except Exception as e:
            # Caso ocorra algum erro inesperado
            response.status_code = 500
            return {"status": "error", "message": "Erro ao atualizar os dados do cliente"}
