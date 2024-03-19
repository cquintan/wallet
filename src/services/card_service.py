from sqlalchemy.orm import Session
from . import database_context
from ..models import card

class CardService():
    def __init__(self):
        self.__database_context = database_context.DatabaseContext()

    def add_card(self, new_card):
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            db.add(new_card)
            db.commit()

    def get_all_cards(self):
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            return db.query(card.Card).all()