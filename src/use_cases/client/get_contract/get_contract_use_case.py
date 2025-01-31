from repositories.contract_repository import ContractRepository
from fastapi import Request, Response

class GetContractUseCase:
    def __init__(self, contract_repository: ContractRepository):
        self.contract_repository =  contract_repository

    def execute(self, response: Response, request: Request):

        contract = self.contract_repository.get_all_contracts()
        if not contract:
            response.status_code = 404
            return {"message": "Nenhum plano encontrada"}
        
        response.status_code = 200
        return contract