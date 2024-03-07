from sqlalchemy import Column, Integer, Float, String, DateTime, Enum
from .transaction_selection import TransactionStatus
from .base import Base

## @brief
#  create a class Transaction in bd Base
class Transaction(Base):
    __tablename__ = "Transaction"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String)        # create properties of the class card number
    transaction_type = Column(Enum(TransactionStatus))      # create properties of the class type of transaction  that determines whether it's a credit or a debit
    transaction_amount = Column(Float)      # create properties of the class amount transaction
    transaction_date_time = Column(DateTime)        # create properties of the class date and time
    sender_recipient = Column(String)       # create properties of the class sender / receiver