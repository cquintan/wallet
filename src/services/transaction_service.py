from sqlalchemy.orm import Session
from . import DatabaseContext
from . import models

## @brief
#  create a class TransactionService
class TransactionService():
    # create a function
    def __init__(self):
        # create a variable  __database_context
        self.__database_context = DatabaseContext()

    # create a function to add a transaction
    def add_transaction(self, transaction):
        # connect to the database
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            # add transaction details
            db.add(transaction)
            # transaction data is sent to the database
            db.commit()

    # create a function to get all data of transactions
    def get_all_transactions(self):
        # connect to the database
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            # all transactions data output
            return db.query(models.Transaction).all()