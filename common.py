from models.header_auth_model import HeaderAuthModel
from peewee import *
from maeapi.maeapi import MAE  # noqa: E402

def getHeaderAuthKey():
    try:
        key = HeaderAuthModel.get(HeaderAuthModel.status == True).key
        if (isHeaderAuthValid(key)):
            return key
        return None
    except DoesNotExist:
        return None

def isHeaderAuthValid(key):
    try:
        MAE(key)
        return True
    except:
        return False