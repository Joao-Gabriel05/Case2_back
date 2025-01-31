import os
import bcrypt
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.client import Client
from models.client_model import ClientsModel
from models.fields.sensivity_field import SensivityField

class ClientsRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    # Salva um novo cliente no banco de dados
    def save(self, client: Client) -> None:
        client_model = ClientsModel()
        client_dict = client.model_dump()

        for k in ClientsModel.get_normal_fields():
            if k not in client_dict:
                continue

            client_model[k] = client_dict[k]

        for k in ClientsModel.sensivity_fields:
            client_model[k] = SensivityField(fernet=self.fernet, data=client_dict[k])

        client_model.password = bcrypt.hashpw(f"{client.password}".encode(), bcrypt.gensalt()).decode()

        client_model.save()

        return None

    # Busca clientes pelo email
    def find_by_email(self, email: str) -> List[ClientsModel]:
        result = ClientsModel.objects(email=email)
        return result

    # Busca clientes pelo ID
    def find_by_id(self, id: str) -> List[ClientsModel]:
        result = ClientsModel.objects(id=id)
        return result

    # Atualiza o token de redefinição de senha
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        ClientsModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None

    # Busca cliente pelo token de redefinição de senha
    def find_by_reset_pwd_token(self, token: str) -> List[ClientsModel]:
        result = ClientsModel.objects(reset_pwd_token=token)
        return result

    # Atualiza a senha de um cliente
    def update_pwd(self, id: str, pwd: str) -> None:
        ClientsModel.objects(id=id).update(set__password=bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None

    # Retorna o nome de um cliente pelo ID
    def get_name(self, id: str) -> str:
        client = ClientsModel.objects(id=id).first()
        if client:
            return client.name

    # Retorna o e-mail de um cliente pelo ID
    def get_email(self, id: str) -> str:
        client = ClientsModel.objects(id=id).first()
        if client:
            return client.email
    
        # Retorna o telefone de um cliente pelo ID
    def get_phone(self, id: str) -> str:
        client = ClientsModel.objects(id=id).first()
        if client:
            return client.phone

    # Retorna a cidade de um cliente pelo ID
    def get_city(self, id: str) -> str:
        client = ClientsModel.objects(id=id).first()
        if client:
            return client.city

    # Retorna o CEP de um cliente pelo ID
    def get_cep(self, id: str) -> str:
        client = ClientsModel.objects(id=id).first()
        if client:
            return client.cep

    # Retorna o número da rua de um cliente pelo ID
    def get_street_number(self, id: str) -> int:
        client = ClientsModel.objects(id=id).first()
        if client:
            return client.street_number
    
        # Retorna o número da rua de um cliente pelo ID
    def get_services(self, id: str) -> int:
        client = ClientsModel.objects(id=id).first()
        if client:
            return client.services

    # Retorna o número da rua de um cliente pelo ID
    def get_cart(self, id: str) -> int:
        client = ClientsModel.objects(id=id).first()
        if client:
            return client.cart


    # Atualiza o nome de um cliente pelo ID
    def update_name(self, id: str, name: str) -> None:
        ClientsModel.objects(id=id).update(set__name=name)
        return None

    # Atualiza o e-mail de um cliente pelo ID
    def update_email(self, id: str, email: str) -> None:
        ClientsModel.objects(id=id).update(set__email=email)
        return None
    
    # Atualiza o número de telefone de um cliente pelo ID
    def update_phone(self, id: str, phone: str) -> None:
        ClientsModel.objects(id=id).update(set__phone=phone)
        return None

    # Atualiza a cidade de um cliente pelo ID
    def update_city(self, id: str, city: str) -> None:
        ClientsModel.objects(id=id).update(set__city=city)
        return None

    # Atualiza o CEP de um cliente pelo ID
    def update_cep(self, id: str, cep: str) -> None:
        ClientsModel.objects(id=id).update(set__cep=cep)
        return None

    # Atualiza o número da rua de um cliente pelo ID
    def update_street_number(self, id: str, street_number: int) -> None:
        ClientsModel.objects(id=id).update(set__street_number=street_number)
        return None
    
        # Atualiza o nome de um cliente pelo ID
    def update_cart(self, id: str, cart: str) -> None:
        ClientsModel.objects(id=id).update(set__cart=cart)
        return None

           # Atualiza o nome de um cliente pelo ID
    def update_services(self, id: str, services: str) -> None:
        ClientsModel.objects(id=id).update(set__services=services)
        return None

    