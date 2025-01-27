import os
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.plan import Plan  # Substitua 'Task' por 'Plan'
from models.plan_model import PlanModel  # Substitua 'TaskModel' por 'PlanModel'
from models.fields.sensivity_field import SensivityField  # Se for necessário usar campos sensíveis

class PlanRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, plan: Plan) -> None:
        plan_model = PlanModel()
        plan_dict = plan.model_dump()  # Isso assume que o modelo 'Plan' tem esse método

        # Salvando os campos normais do modelo de planos
        for k in PlanModel.get_normal_fields():  # Substitua get_normal_fields() conforme necessário
            if k not in plan_dict:
                continue
            plan_model[k] = plan_dict[k]

        # Salvando campos sensíveis, se houver
        for k in PlanModel.sensivity_fields:
            if k in plan_dict:
                plan_model[k] = SensivityField(fernet=self.fernet, data=plan_dict[k])

        plan_model.save()
        return None

    def get_plan_by_id(self, plan_id: str) -> dict:
        plan = PlanModel.objects.with_id(plan_id)
        if not plan:
            return None
        plan_dict = plan.to_mongo().to_dict()
        plan_dict['_id'] = str(plan_dict['_id'])
        return plan_dict

    def update(self, plan_id: str, updated_data: dict) -> None:
        plan = PlanModel.objects.with_id(plan_id)
        if not plan:
            raise ValueError("Plano não encontrado")
        updated_data = updated_data.model_dump()  # Se precisar, pode ajustar esse método conforme necessário
        for key, value in updated_data.items():
            if hasattr(plan, key):
                setattr(plan, key, value)

        plan.save()

    def get_all_plans(self) -> List[dict]:
        plans = PlanModel.objects()
        result = []

        for plan in plans:
            plan_dict = plan.to_mongo().to_dict()
            plan_dict['_id'] = str(plan_dict['_id']) 
            result.append(plan_dict)

        return result

    def delete_plan(self, plan_id: str) -> bool:
        plan = PlanModel.objects.with_id(plan_id)
        if not plan:
            return False
        plan.delete()
        return True
