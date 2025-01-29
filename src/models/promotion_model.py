from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class PromotionModel(Document):
    sensivity_fields = [
        
    ]
    description = StringField(required=True) 
    plan = ListField(StringField(), required=True)
    price = FloatField(required=True)
    old_price = FloatField(required=True)


    



    def get_normal_fields():
        return [i for i in PromotionModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in PromotionModel.sensivity_fields]
    
