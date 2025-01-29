from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class ContractModel(Document):
    sensivity_fields = [
        
    ]

    plan = StringField(required=True)
    client = StringField(required=True)
    start_date = DateField(required=True)



    



    def get_normal_fields():
        return [i for i in ContractModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in ContractModel.sensivity_fields]
    
