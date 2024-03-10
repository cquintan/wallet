## @package banc_account_service
#  @brief Business logic of working with account, adding and deleting accouns from the database.

## @brief Using a session to work with the database.
from sqlalchemy.orm import Session
## @brief Using the service to work with the database.
from . import database_context
## @brief Using BankAccount model.
from ..models import bank_account

## @brief Account Handling Service.
#  @details Adding user accounts to the database, to configure permissions and user account access settings, to register users.
class BankAccountService():
    ## @brief The constructor.
    #  @param[in] self The object pointer.
    def __init__(self):
        ## @brief Database instance for working with the database.
        self.__database_context = database_context.DatabaseContext()

    ## @brief Adding an instance of the bank account class to the database.
    #  @param[in] self The object pointer.
    #  @param[in] account The BankAccount class instance.
    def add_bank_account(self, account):
        ## @brief Check that the account parameter is an instance of the BankAccount class.
        if isinstance(account, bank_account.BankAccount):
            ## @brief Creating a session to work to the database.
            #  @arg @c autoflush Automatic synchronisation of sessions with the database.
            #  @arg @c bind Link to the database core.
            with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
                ## @brief Creating a request to add a account to the database.
                db.add(account)
                ## @brief Sending all queries to the database for execution.
                db.commit()

    ## @brief Sending all queries to the database for execution.
    def get_all_bank_account(self):
        ## @brief Creating a session to work to the database.
        #  @arg @c autoflush Automatic synchronisation of sessions with the database.
        #  @arg @c bind Link to the database core.
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            ## @brief Get all bank_accounts.
            return db.query(bank_account.BankAccount).all()