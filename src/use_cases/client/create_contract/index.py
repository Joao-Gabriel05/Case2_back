from repositories.contract_repository import ContractRepository
from .create_contract_dto import CreateContractDTO
from .create_contract_use_case import CreateContractUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_contract_use_case = CreateContractUseCase(ContractRepository())

@router.post("/client/create-contract")
def create_contract(create_contract_dto:CreateContractDTO, response:Response, request:Request):
    return create_contract_use_case.execute(create_contract_dto, response, request)

