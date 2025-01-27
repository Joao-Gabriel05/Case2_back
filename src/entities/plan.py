import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Plan(BaseModel):
    _id: str
    type: Literal["fibra","5G","4G"]
    speed : str
    details : List[str]


