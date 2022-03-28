from datetime import datetime
from dateutil.relativedelta import relativedelta
from common import getHeaderAuthKey
from maeapi.maeapi import MAE  # noqa: E402
from models.transaction_model import TransactionModel
# checkis api valid

if(getHeaderAuthKey()):
    mae = MAE(getHeaderAuthKey())
    dateFormat = "%Y%m%d"

    fromdate = datetime.strptime('20210101',dateFormat)

    while True:
       
        fromdate = fromdate
        todate = fromdate + relativedelta(months=+2)
        print(fromdate)
        print(todate)
        if (fromdate < datetime.now()):
            print(fromdate.strftime)
            transaction = mae.get_transaction_history(
                fromdate.strftime(dateFormat), 
                todate.strftime(dateFormat))
            for i in transaction:
                
                txn = TransactionModel.replace(
                    btsId=i['btsId'],
                    transactionDate= i['transactionDate'],
                    amount = i['amount'],
                    btsDescription = i['btsDescription']
                ).execute()
            fromdate = todate
        if (fromdate > datetime.now()):
            break
         
        