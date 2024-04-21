## @package test_user_service
#  @brief We test the work of the file user_sevice.py to add and output login and hashed password to the database to build business logic and systematization of data.

## @brief Using a session for testing .
import pytest
## @brief Using a session to be able to automate the date and time
import datetime
## @brief Using models that import context.
from context import models
## @brief Using services that import context.
from context import services
## @brief Using a session to work with the database.
from sqlalchemy.orm import Session

## @brief User registration testing.
#  @details Testing adding login and hashed password to the database, outputting all logins and all hashed passwords from the database, as well as the table with user data.
class TestUserService():
    ## @brief Create a fixture to further clean up the table in the database after testing.
    #  @param[in] self The object pointer.
    @pytest.fixture
    def user_table_cleanup(self):
        ## @brief Creating a session to work to the database.
        #  @arg @c autoflush Automatic synchronisation of sessions with the database.
        #  @arg @c bind Link to the database core.
        with Session(autoflush=False, bind=services.database_context.DatabaseContext().database_engine) as db:
            ## @brief Create a query to clean up the User table in the database.
            db.query(models.user.User).delete()
            ## @brief Send all queries to the database for execution.
            db.commit()

    ## @brief Testing adding a user to the database.
    #  @param[in] self The object pointer.
    #  @param[in] Fixture to clear the User table of logins and passwords added during the test.
    def test_add_user(self, user_table_cleanup):
        ## @brief Create a login for the test.
        sample_login = "sample-login"
        ## @brief Create a password for the test.
        sample_password = "sample-password"

        ## @brief Database instance for working with the database.
        sample_user_service = services.user_service.UserService()
        ## @brief Pass the test login and test password to the database.
        assert sample_user_service.add_user(sample_login, sample_password)

    ## @brief Testing the output of user data from the database.
    #  @param[in] self The object pointer.
    #  @param[in] Fixture to clear the User table of logins and passwords added during the test.
    def test_get_all_user(self, user_table_cleanup):
        ## @brief Create a login for the test.
        sample_login = "sample-login"
        ## @brief Create a password for the test.
        sample_password = "sample-password"

        ## @brief Database instance for working with the database.
        sample_user_service = services.user_service.UserService()
        ## @brief Pass the test login and test password to the database.
        sample_user_service.add_user(sample_login, sample_password)
        sample_user = sample_user_service.get_all_users()
        assert sample_login == sample_user[0].login

    ## @brief User Authorization Testing.
    #  @param[in] self The object pointer.
    #  @param[in] Fixture to clear the User table of logins and passwords added during the test.
    def test_login_user(self, user_table_cleanup):
        ## @brief Create a login for the test.
        sample_login = "sample-login"
        ## @brief Create a password for the test.
        sample_password = "sample-password"

        ## @brief Database instance for working with the database.
        sample_user_service = services.user_service.UserService()
        ## @brief Adding a test user to the database.
        sample_user_service.add_user(sample_login, sample_password)
        ## @brief Attempting to log in with test credentials.
        assert sample_user_service.login_user(sample_login, sample_password) == True

if __name__ == "__main__":
    pytest.main()
