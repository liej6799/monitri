from models.header_auth_model import HeaderAuthModel
from peewee import *


def getkey():
    try:
        return  HeaderAuthModel.get(HeaderAuthModel.status == True).key
    except DoesNotExist:
        return None

