from pydantic import BaseModel
from typing import Literal, Optional

class CreateTaskDTO(BaseModel):
    _id: str
    status: Literal["pendente","em progresso","finalizada"]
    priority : Literal["pouco importante","importante","muito importante"]
    title:str
    due_date: str
