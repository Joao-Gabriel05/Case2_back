from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class PlanModel(Document):
    sensivity_fields = [
        
    ]

    type = StringField(required=True, choices=["fibra", "5G", "4G"])
    speed = StringField(required=True)
    details = ListField(StringField(), required=True) 


    



    def get_normal_fields():
        return [i for i in TaskModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in TaskModel.sensivity_fields]
    
