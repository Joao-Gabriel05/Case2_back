import dotenv
from pydantic import BaseModel
from datetime import date  # Para trabalhar com o tipo date
from typing import Literal, Optional, List

dotenv.load_dotenv()

class UpdateCartDTO(BaseModel):   
    cart : List[str]
