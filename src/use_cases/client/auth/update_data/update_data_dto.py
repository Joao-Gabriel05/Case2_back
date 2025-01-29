import dotenv
from pydantic import BaseModel
from datetime import date  # Para trabalhar com o tipo date
from typing import Literal, Optional, List

dotenv.load_dotenv()

class UpdateClientDTO(BaseModel):   
    name: str
    email: str
    phone: str
    birth_date: date
    cpf: str  
    city:str
    CEP: str
    street_number:int
    password: str
    services: List[str]
