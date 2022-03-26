from peewee import *


db = SqliteDatabase('monitri.db')

class BaseModel(Model):
    class Meta:
        database = db
