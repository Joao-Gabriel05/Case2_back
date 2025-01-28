import dotenv
from pydantic import BaseModel, ConfigDict
from datetime import date  # Para trabalhar com o tipo date
from typing import Literal, Optional, List

dotenv.load_dotenv()

class LoginDTO(BaseModel):
    cpf : int
    password: str