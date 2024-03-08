from sqlalchemy import Column, Integer, Float, String
from .base import Base
## @brief
#  create a class Card in bd Base
class Card(Base):
    __tablename__ = "Card"
    id = Column(Integer, primary_key=True, index=True)
    # create properties of the class card number
    card_number = Column(String)
    # create properties of the class card owner
    card_owner = Column(String)
    # create properties of the class cvv code
    cvv_code = Column(Integer)
    # create properties of the class card balance
    card_balance = Column(Float)
    