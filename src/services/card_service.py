from sqlalchemy.orm import Session
from . import DatabaseContext
from . import models

## @brief
#  create a class CardService
class CardService():
    ## create a function
    def __init__(self):
        ## create a variable  __database_context
        self.__database_context = DatabaseContext()

    ## create a function to add a card
    def add_card(self, card):
        # connect to the database
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            # add card details
            db.add(card)
            # card data is sent to the database
            db.commit()

    # create a function to get all data of cards
    def get_all_cards(self):
        # connect to the database
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:
            # all card data output
            return db.query(models.Card).all()