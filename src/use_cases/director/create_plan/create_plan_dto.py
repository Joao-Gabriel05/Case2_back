from pydantic import BaseModel
from typing import Literal, Optional,List

class CreatePlanDTO(BaseModel):
    _id: str
    type: Literal["fibra","5G","4G"]
    speed : str
    details : List[str]
    price : float
    public: Literal["B2B","B2C"]
