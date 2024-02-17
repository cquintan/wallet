from sqlalchemy import Column, Integer, Float, String
from . import Base

class Card(Base):
    __tablename__ = "Card"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String)
    card_owner = Column(String)
    cvv_code = Column(Integer)
    card_balance = Column(Float)