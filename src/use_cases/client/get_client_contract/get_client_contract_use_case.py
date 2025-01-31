from repositories.contract_repository import ContractRepository
from fastapi import Request, Response
from entities.contract import Contract

class GetClientContractUseCase:
    def __init__(self, contract_repository: ContractRepository):
        self.contract_repository = contract_repository

    def execute(self, client_id: str, response: Response, request: Request):

        contracts = self.contract_repository.get_contracts_by_user_id(client_id)
        if not contracts:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return contracts