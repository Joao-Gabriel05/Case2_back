import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
from datetime import date  # Para trabalhar com o tipo date
dotenv.load_dotenv()

class Contract(BaseModel):
    _id: str
    plan: str 
    start_date: date
    used: Optional[str] = "0 GB"


