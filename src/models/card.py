from sqlalchemy import Column, Integer, Float, String
from . import base

class Card(base.Base):
    __tablename__ = "Card"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String)
    card_owner = Column(String)
    cvv_code = Column(Integer)
    card_balance = Column(Float)