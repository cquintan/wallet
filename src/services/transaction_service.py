## @package transaction_service
#  @brief Business logic of working with transactions, adding and deleting transactions from the database.

## @brief Using a session to work with the database.
from sqlalchemy.orm import Session
## @brief Using the service to work with the database.
from . import database_context
## @brief Using Transaction model.
from ..models import transaction

## @brief Transaction handling service.
#  @details Adding transactions to the database, using transaction data it is possible to create a history of bank operations.
class TransactionService():
    ## @brief The constructor.
    #  @param[in] self The object pointer.
    def __init__(self):
        ## @brief Database instance for working with the database.
        self.__database_context = database_context.DatabaseContext()

    ## @brief Adding a transaction class instance to the database.
    #  @param[in] self The object pointer.
    #  @param[in] new_transaction The Transaction class instance.
    def add_transaction(self, new_transaction):
        ## @brief Check that the transaction parameter is an instance of the Transaction class.
        if isinstance(new_transaction, transaction.Transaction):
            ## @brief Creating a session to work to the database.
            #  @arg @c autoflush Automatic synchronisation of sessions with the database.
            #  @arg @c bind Link to the database core.
            with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
                ## @brief Creating a request to add a new_transaction to the database.
                db.add(new_transaction)
                ## @brief Sending all queries to the database for execution.
                db.commit()
                return True
        return False

    ## @brief Sending all queries to the database for execution.
    def get_all_transactions(self):
        ## @brief Creating a session to work to the database.
        #  @arg @c autoflush Automatic synchronisation of sessions with the database.
        #  @arg @c bind Link to the database core.
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            ## @brief Get all transactions.
            return db.query(transaction.Transaction).all()