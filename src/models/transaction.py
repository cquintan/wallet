from sqlalchemy import Column, Integer, Float, String, DateTime, Enum
from .transaction_selection import TransactionStatus
from .base import Base


class Transaction(Base):
    __tablename__ = "Transaction"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String)
    transaction_type = Column(Enum(TransactionStatus))
    transaction_amount = Column(Float)
    transaction_date_time = Column(DateTime)
    sender_recipient = Column(String)