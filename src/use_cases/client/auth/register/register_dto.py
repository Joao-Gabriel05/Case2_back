import dotenv
from pydantic import BaseModel, ConfigDict
from datetime import date  # Para trabalhar com o tipo date
from typing import Literal, Optional, List

dotenv.load_dotenv()

class RegisterDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    email: str
    phone: str
    birth_date: date
    cpf: int
    city: str
    CEP: str
    street_number: int
    password: str
    services: Optional[List[str]] = []  # Se não fornecido, será uma lista vazia
    invoices: Optional[List[str]] = []  # Se não fornecido, será uma lista vazia
