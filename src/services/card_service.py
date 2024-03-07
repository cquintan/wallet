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
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:      #connect to the database
            db.add(card)        #add card details
            db.commit()         # card data is sent to the database

    def get_all_cards(self):        #create a function to get all data of cards
        with Session(autoflush=False, bind=self.__database_context.database_engine) as db:      #connect to the database
            return db.query(models.Card).all()      #all card data output