import dotenv
from pydantic import BaseModel
from datetime import date  # Para trabalhar com o tipo date
from typing import Literal, Optional, List

dotenv.load_dotenv()

class UpdateClientDTO(BaseModel):   
    phone: str 
    city:str
    cep: str
    street_number:int
