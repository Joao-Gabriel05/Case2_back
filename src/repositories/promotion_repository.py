import os
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.promotion import Promotion  # Substitua 'Plan' por 'Promotion'
from models.promotion_model import PromotionModel  # Substitua 'PlanModel' por 'PromotionModel'
from models.fields.sensivity_field import SensivityField  # Se necessário para campos sensíveis

class PromotionRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, promotion: Promotion) -> None:
        promotion_model = PromotionModel()
        promotion_dict = promotion.model_dump()  # Isso assume que o modelo 'Promotion' tem esse método

        # Salvando os campos normais do modelo de promoções
        for k in PromotionModel.get_normal_fields():  # Substitua get_normal_fields() conforme necessário
            if k not in promotion_dict:
                continue
            promotion_model[k] = promotion_dict[k]

        # Salvando campos sensíveis, se houver
        for k in PromotionModel.sensivity_fields:
            if k in promotion_dict:
                promotion_model[k] = SensivityField(fernet=self.fernet, data=promotion_dict[k])

        promotion_model.save()
        return None

    def get_promotion_by_id(self, promotion_id: str) -> dict:
        promotion = PromotionModel.objects.with_id(promotion_id)
        if not promotion:
            return None
        promotion_dict = promotion.to_mongo().to_dict()
        promotion_dict['_id'] = str(promotion_dict['_id'])
        return promotion_dict

    def update(self, promotion_id: str, updated_data: dict) -> None:
        promotion = PromotionModel.objects.with_id(promotion_id)
        if not promotion:
            raise ValueError("Promoção não encontrada")
        updated_data = updated_data.model_dump()  # Se precisar, ajuste este método conforme necessário
        for key, value in updated_data.items():
            if hasattr(promotion, key):
                setattr(promotion, key, value)

        promotion.save()

    def get_all_promotions(self) -> List[dict]:
        promotions = PromotionModel.objects()
        result = []

        for promotion in promotions:
            promotion_dict = promotion.to_mongo().to_dict()
            promotion_dict['_id'] = str(promotion_dict['_id'])
            result.append(promotion_dict)

        return result

    def delete_promotion(self, promotion_id: str) -> bool:
        promotion = PromotionModel.objects.with_id(promotion_id)
        if not promotion:
            return False
        promotion.delete()
        return True
