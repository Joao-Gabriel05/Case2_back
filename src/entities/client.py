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
    birth_date: str
    cpf: str 
    city: str
    cep: str
    street_number: str
    password: str
    services: Optional[List[str]] = [] 
    cart : Optional[List[str]] = [] 

    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0