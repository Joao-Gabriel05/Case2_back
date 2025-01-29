import dotenv
from pydantic import BaseModel, ConfigDict
from typing import Literal, Optional, List

dotenv.load_dotenv()

class RegisterDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    email: str
    phone: str# O campo é opcional
    birth_date: str  # O campo é opcional
    cpf: str  # O campo é opcional
    city: str# O campo é opcional
    cep: str  # O campo é opcional
    street_number: str # O campo é opcional
    password: str
    services: Optional[List[str]] = []  # O campo é opcional, com valor padrão sendo uma lista vazia
    cart: Optional[List[str]] = []  # O campo é opcional, com valor padrão sendo uma lista vazia