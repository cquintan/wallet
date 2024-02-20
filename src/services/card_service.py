from sqlalchemy.orm import Session
from . import DatabaseContext
from . import models

class CardService():
    def __init__(self):
        self.__database_context = DatabaseContext()
    def add_card(self, card):
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            db.add(card)
            db.commit()

    def get_all_cards(self):
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            return db.query(models.Card).all()