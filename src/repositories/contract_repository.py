import os
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.contract import Contract  # Substitua 'Plan' por 'Contract'
from models.contract_model import ContractModel  # Substitua 'PlanModel' por 'ContractModel'
from models.fields.sensivity_field import SensivityField  # Se for necessário usar campos sensíveis

class ContractRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, contract: Contract) -> None:
        contract_model = ContractModel()
        contract_dict = contract.model_dump()  # Isso assume que o modelo 'Contract' tem esse método

        # Salvando os campos normais do modelo de contratos
        for k in ContractModel.get_normal_fields():  # Substitua get_normal_fields() conforme necessário
            if k not in contract_dict:
                continue
            contract_model[k] = contract_dict[k]

        # Salvando campos sensíveis, se houver
        for k in ContractModel.sensivity_fields:
            if k in contract_dict:
                contract_model[k] = SensivityField(fernet=self.fernet, data=contract_dict[k])

        contract_model.save()
        return None

    def get_contract_by_id(self, contract_id: str) -> dict:
        contract = ContractModel.objects.with_id(contract_id)
        if not contract:
            return None
        contract_dict = contract.to_mongo().to_dict()
        contract_dict['_id'] = str(contract_dict['_id'])
        return contract_dict

    def update(self, contract_id: str, updated_data: dict) -> None:
        contract = ContractModel.objects.with_id(contract_id)
        if not contract:
            raise ValueError("Contrato não encontrado")
        updated_data = updated_data.model_dump()  # Se precisar, pode ajustar esse método conforme necessário
        for key, value in updated_data.items():
            if hasattr(contract, key):
                setattr(contract, key, value)

        contract.save()

    def get_all_contracts(self) -> List[dict]:
        contracts = ContractModel.objects()
        result = []

        for contract in contracts:
            contract_dict = contract.to_mongo().to_dict()
            contract_dict['_id'] = str(contract_dict['_id']) 
            result.append(contract_dict)

        return result

    def delete_contract(self, contract_id: str) -> bool:
        contract = ContractModel.objects.with_id(contract_id)
        if not contract:
            return False
        contract.delete()
        return True

    def get_contracts_by_user_id(self, client_id: str) -> List[dict]:
        # Buscando contratos onde o campo 'user' é igual ao 'user_id' fornecido
        contracts = ContractModel.objects(client=client_id)
        result = []

        for contract in contracts:
            contract_dict = contract.to_mongo().to_dict()
            contract_dict['_id'] = str(contract_dict['_id'])  # Convertendo o ObjectId para string
            result.append(contract_dict)

        return result
