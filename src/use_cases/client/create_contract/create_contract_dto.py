import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
from datetime import date  # Para trabalhar com o tipo date
dotenv.load_dotenv()

class CreateContractDTO(BaseModel):
    plan: str 
    client: str
    start_date: date
    used: Optional[str] = None


