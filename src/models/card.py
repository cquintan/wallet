from sqlalchemy import Column, Integer, Float, String
from .base import Base
## @brief
#  create a class Card in bd Base
class Card(Base):
    __tablename__ = "Card"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String)        # create properties of the class card number
    card_owner = Column(String)         # create properties of the class card owner
    cvv_code = Column(Integer)          # create properties of the class cvv code
    card_balance = Column(Float)        # create properties of the class card balance
    