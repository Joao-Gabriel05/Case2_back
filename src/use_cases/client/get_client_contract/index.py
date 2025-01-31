from repositories.contract_repository import ContractRepository
from .get_client_contract_use_case import GetClientContractUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_contracts_use_case= GetClientContractUseCase(ContractRepository())

@router.get("/client/get-client-contracts/{client_id}")
def get_plan( client_id:str,response:Response, request:Request):
    return get_contracts_use_case.execute(client_id,response, request)
