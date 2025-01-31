from repositories.contract_repository import ContractRepository
from .get_contract_by_id_use_case import GetContractByIDUseCase
from .get_contract_use_case import GetContractUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_contract_by_id_use_case = GetContractByIDUseCase(ContractRepository())
get_contract_use_case = GetContractUseCase(ContractRepository())

@router.get("/client/get-contract/{contract_id}")
def get_contract_by_id(contract_id: str ,response:Response, request:Request):
    return get_contract_by_id_use_case.execute(contract_id,response, request)

@router.get("/client/get-contract")
def get_contract(response:Response, request:Request):
    return get_contract_use_case.execute(response, request)