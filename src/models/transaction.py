## @package transaction
#  @brief A model that represents transactions in a database.

## @brief Using types to work with orm.
from sqlalchemy import Column, Integer, Float, String, DateTime, Enum
## @brief Using base model.
from . import TransactionStatus
## @brief Using base model.
from . import TransactionType
## @brief Using base model.
from . import Base

## @brief Transaction
#  @details Transactions are the main types of operations on the user's account, thanks to them it is possible to analyze expenses and income, as well as to work with the user's account to add and deduct funds from the account.
#  <br />Transactions are inherited from the base model.
class Transaction(Base):
    ## @brief Database table name.
    __tablename__ = "Transaction"
    ## @brief Primary key for indexing in the database.
    id = Column(Integer, primary_key=True, index=True)
    ## @brief Bank card number.
    card_number = Column(String)
    ## @brief Transaction type debit or credit type.
    card_transaction = Column(Enum(TransactionStatus))
    ## @brief Bank card transaction amount.
    transaction_amount = Column(Float)
    ## @brief Date and time of the card transaction made.
    transaction_date_time = Column(DateTime)
    ## @brief Transaction type, spend category and enrollment category.
    transaction_type = Column(Enum())
    ## @brief Who is the recipient and sender on the transaction.
    recipient_sender = Column(String)

