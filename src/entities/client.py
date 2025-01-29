import dotenv
from pydantic import BaseModel
from datetime import date  # Para trabalhar com o tipo date
from typing import Literal, Optional, List

dotenv.load_dotenv()

class Client(BaseModel):
    _id: str
    name: str
    email: str
    phone: str
    birth_date: date  # Definindo birth_date como uma data
    cpf : int
    city: str
    CEP: str
    street_number: int
    password: str
    services:List[str]

    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0