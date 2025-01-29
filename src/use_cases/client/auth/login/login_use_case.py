from repositories.client_repository import ClientsRepository
from fastapi import FastAPI, Request, Response
from use_cases.client.auth.login.login_dto import LoginDTO
from entities.director import Director
import jwt
import os

class LoginUseCase:
    client_repository: ClientsRepository

    def __init__(self, client_repository: ClientsRepository):
        self.client_repository = client_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        check_exists = self.client_repository.find_by_email(email=login_dto.email)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um cliente com o email fornecido"}

        cliente = check_exists[0]

        if (not cliente.check_password_matches(login_dto.password)):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}

        token = jwt.encode({"email": cliente.email, "id": str(cliente.id)}, os.getenv("CLIENT_JWT_SECRET"))

        response.set_cookie(key="client_auth_token", value=f"Bearer {token}", httponly=True)
        
        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}