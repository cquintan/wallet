## @package bank_account
#  @brief Model representing a bank account in the database.

## @brief Using types to work with orm.
from sqlalchemy import Column, Integer, String
## @brief Using base model.
from . import Base

## @brief Bank account
#  @details Bank account - this is the user's account number, bank cards can be linked to this account.
#  <br />Bank account is inherited from the base model.
class BankAccount(Base):
    ## @brief Database table name.
    __tablename__ = "BankAccount"
    ## @brief Primary key for indexing in the database.
    id = Column(Integer, primary_key=True, index=True)
    ## @brief Bank account number.
    bank_account_number = Column(String)
    ## @brief Bank account holder.
    bank_account_owner = Column(String)