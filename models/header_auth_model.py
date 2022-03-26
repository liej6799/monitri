
import datetime
from peewee import CharField, IntegerField, DateField, BooleanField
from models.base_model import BaseModel

class HeaderAuthModel(BaseModel):
    key = CharField(unique=True)
    status = BooleanField(default=True)
    lastupdateddatetime = DateField(default=datetime.datetime.now)