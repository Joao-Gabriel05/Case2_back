import dotenv
from pydantic import BaseModel
from datetime import date  # Para trabalhar com o tipo date
from typing import Literal, Optional, List

dotenv.load_dotenv()

class UpdateClientByDTO(BaseModel):   
    services: List[str]
    cart : List[str]
