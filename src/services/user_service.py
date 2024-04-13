## @package registration
#  @brief Add user accounts with to build business logic and individualize access to personal data.

## @brief Using a session to work with the database.
from sqlalchemy.orm import Session
## @brief Using the service to work with the database.
from . import database_context
## @brief Using User model.
from ..models import user
## @brief Using the hashing library.
import hashlib

## @brief Registration service.
#  @details By adding users to the database, whose logins and passwords can be used to personalize access to bank card data and account history.
class UserService():
    ## @brief The constructor.
    #  @param[in] self The object pointer.

    def __init__(self):
        ## @brief Database instance for working with the database.
        self.__database_context = database_context.DatabaseContext()

    def __check_user__(self, user):
        comparison = Session.query(exists().where(user.login == login, user.password == password)).scalar()
        if comparison != None:
            return True
        return False

    ## @brief Adding a registration class instance to the database.
    #  @param[in] self The object pointer.
    #  @param[in] user The User class instance.
    def add_user(self, login, password):
        user_password_login = user.User(login=login, password=hashlib.sha3_512(f'{password}'.encode('utf-8')).hexdigest())

        ## @brief Creating a session to work to the database.
        #  @arg @c autoflush Automatic synchronisation of sessions with the database.
        #  @arg @c bind Link to the database core.
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            ## @brief Creating a request to add a user to the database.
            db.add(user_password_login)
            ## @brief Sending all queries to the database for execution.
            db.commit()
            return True

    ## @brief Sending all queries to the database for execution.
    def get_all_users(self):
        ## @brief Creating a session to work to the database.
        #  @arg @c autoflush Automatic synchronisation of sessions with the database.
        #  @arg @c bind Link to the database core.
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            ## @brief Get all users.
            return db.query(user.User).all()