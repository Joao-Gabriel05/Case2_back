from pydantic import BaseModel
from typing import Literal, Optional,List

class CreatePlanDTO(BaseModel):
    type: Literal["Telfonia Fixa","Banda","movel-5G","movel-4G"]
    speed : str
    details : List[str]
    price : float
    public: Literal["B2B","B2C"]
    products: Optional[List[str]] = [] 
