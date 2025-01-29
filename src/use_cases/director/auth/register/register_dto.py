from pydantic import BaseModel, ConfigDict

class RegisterDTO(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    email: str
    cpf: str 
    password: str