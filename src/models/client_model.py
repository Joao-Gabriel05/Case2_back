from mongoengine import *
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet
import datetime

from mongoengine import Document, StringField, DateField, IntField, ListField
dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class ClientsModel(Document):
    # Campos sensíveis que devem ser criptografados
    sensivity_fields = [

    ]
    # Campos do modelo
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    phone = StringField(required=True)  # Torna o campo opcional e com valor padrão null
    birth_date = StringField(required=True)  # Torna o campo opcional e com valor padrão null
    cpf = StringField(required=True, unique=True)  # Torna o campo opcional e com valor padrão null
    city = StringField(required=True)  # Torna o campo opcional e com valor padrão null
    cep = StringField(required=True)  # Torna o campo opcional e com valor padrão null
    street_number = StringField(required=True)  # Torna o campo opcional e com valor padrão null
    password = StringField(required=True)
    
    # Tornando 'services' opcional, com valor padrão como uma lista vazia, mas pode ser null
    services = ListField(StringField(), required=False, default=[])  # Aqui 'None' pode ser um valor nulo



    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)

    meta = {"collection": "clients"}  # Nome da coleção no MongoDB

    # Obtém campos normais (não sensíveis)
    @staticmethod
    def get_normal_fields():
        return [
            i
            for i in ClientsModel.__dict__.keys()
            if i[:1] != "_"
            and i != "sensivity_fields"
            and i not in ClientsModel.sensivity_fields
        ]

    # Descriptografa um campo sensível
    def get_decrypted_field(self, field: str):
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped")
        return fernet.decrypt(getattr(self, field, None).encode()).decode()

    # Verifica se a senha fornecida coincide com a senha armazenada
    def check_password_matches(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    # Criptografa os campos sensíveis antes de salvar no banco
    def save(self, *args, **kwargs):
        for field in self.sensivity_fields:
            if getattr(self, field, None):
                setattr(self, field, fernet.encrypt(str(getattr(self, field)).encode()).decode())
        super().save(*args, **kwargs)
