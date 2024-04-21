## @package Card
# @brief A model representing the basic account information in the database.

## @brief Using types to work with orm.
from sqlalchemy import Column, Integer, Float, String
## @brief Using base model.
from . import base

## @brief Cards
# @details Card data is the basic information about the user account, thanks to which you can build business logic and store basic information and distinguish between cards and user accounts.
class Card(base.Base):
    ## @brief Database table name.
    __tablename__ = "Card"
    ## @brief Primary key for indexing in the database.
    id = Column(Integer, primary_key=True, index=True)
    ## @brief Bank card number.
    card_number = Column(String)
    ## @brief Bank card owner.
    card_owner = Column(String)
    ## @brief Bank card cvv code.
    cvv_code = Column(Integer)
    ## @brief Bank card balance.
    card_balance = Column(Float)