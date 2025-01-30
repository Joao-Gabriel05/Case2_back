from repositories.contract_repository import ContractRepository  # Repositório de contratos
from use_cases.client.create_contract.create_contract_dto import CreateContractDTO  # DTO para o contrato
from fastapi import Request, Response
from entities.contract import Contract as ContractEntity  # Entidade de contrato

class CreateContractUseCase:
    def __init__(self, contract_repository: ContractRepository):
        self.contract_repository = contract_repository

    def execute(self, create_contract_dto: CreateContractDTO, response: Response, request: Request):
        # Verificar se todos os campos obrigatórios foram preenchidos
        if not create_contract_dto.plan or not create_contract_dto.client or not create_contract_dto.start_date:
            response.status_code = 407
            return {"status": "error", "message": "faltam informações"}

        # Criar a instância do contrato
        contract = ContractEntity(
            plan=create_contract_dto.plan,
            client=create_contract_dto.client,
            start_date=create_contract_dto.start_date,
            used = create_contract_dto.used
        )

        # Salvar o contrato no repositório
        self.contract_repository.save(contract)
        
        # Retornar resposta de sucesso
        response.status_code = 201
        return {"status": "success", "message": "Contrato criado"}
