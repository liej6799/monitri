
import datetime
from peewee import CharField, IntegerField, DateField, BooleanField, FloatField
from models.base_model import BaseModel

class TransactionModel(BaseModel):
    btsId = CharField(unique=True)
    transactionDate = DateField()
    amount = FloatField()
    btsDescription = CharField()
    status = BooleanField(default=True)
    lastupdateddatetime = DateField(default=datetime.datetime.now)