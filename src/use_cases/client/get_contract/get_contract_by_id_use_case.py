from repositories.contract_repository import ContractRepository
from fastapi import Request, Response
from entities.contract import Contract

class GetContractByIDUseCase:
    def __init__(self, contract_repository: ContractRepository):
        self.contract_repository = contract_repository

    def execute(self, contract_id: str, response: Response, request: Request):

        contract = self.contract_repository.get_contract_by_id(contract_id)
        if not contract:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return contract