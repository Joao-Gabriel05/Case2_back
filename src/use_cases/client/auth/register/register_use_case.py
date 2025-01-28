from repositories.client_repository import ClientsRepository
from use_cases.client.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.client import Client

class RegisterUseCase:
    def __init__(self, clients_repository: ClientsRepository):
        self.clients_repository = clients_repository

    def execute(self, register_dto: dict, response: Response, request: Request):
        if (not register_dto.name or not register_dto.password or not register_dto.cpf or not register_dto.email or not register_dto.phone or not register_dto.birth_date or
        not register_dto.CEP or not register_dto.city or not register_dto.street_number or not register_dto.plans or not register_dto.invoices):
            response.status_code = 406
            return {"status": "error", "message": f"Cadastro não realizado, dados estão faltando."}

        client = Client(**register_dto.model_dump())

        self.clients_repository.save(client)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro de cliente com sucesso"}