from sqlalchemy.orm import Session
from . import DatabaseContext
from . import models

## @brief
#  create a class TransactionService
class TransactionService():
    def __init__(self):     #create a function
        self.__database_context = DatabaseContext()     #create a variable  __database_context

    def add_transaction(self, transaction):     #create a function to add a transaction
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:      #connect to the database
            db.add(transaction)     #add transaction details
            db.commit()         # transaction data is sent to the database

    def get_all_transactions(self):     #create a function to get all data of transactions
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:       #connect to the database
            return db.query(models.Transaction).all()       #all transactions data output