from models.base_model import db
from models.header_auth_model import HeaderAuthModel

db.connect()
db.drop_tables([HeaderAuthModel])
db.create_tables([HeaderAuthModel])