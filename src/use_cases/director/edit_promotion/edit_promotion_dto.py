import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class EditPromotionDTO(BaseModel):
    _id: str
    description: str
    plan: List[str]
    price: float


