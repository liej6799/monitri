from models.base_model import db
from models.transaction_model import TransactionModel

db.connect()
db.drop_tables([TransactionModel])
db.create_tables([TransactionModel])