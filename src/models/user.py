## @package user
#  @brief Model representing a user in a database.

## @brief Using types to work with orm.
from sqlalchemy import Column, Integer, String
## @brief Using base model.
from . import Base

## @brief User
#  @details User is user data that can be linked bank cards.
#  <br />The user is inherited from the base model..
class User(Base):
    ## @brief Database table name.
    __tablename__ = "User"
    ## @brief Primary key for indexing in the database.
    id = Column(Integer, primary_key=True, index=True)
    ## @brief User account password.
    password = Column(String)
    ## @brief User account login.
    login = Column(String)