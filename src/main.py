import random
##@brief
#created a class and filled it with parameters
#enter what type of data will be
#
class Card:
    __card_number: str
    __card_owner: str
    __cvv_code: int
    __card_balance: float


    ##@brief
    # create a function for adding money to the card
    # @param [in] cvv_code Card CVV code
    # @param [in] card_owner Card Owner
    def __init__(self, cvv_code, card_owner = 'Default') -> None:
        self.__card_number = self.__create_random_card_number()         ## initialization of the card number parameter
        self.__card_owner = card_owner                                  ## initialization of the card owner parameter
        self.__cvv_code = cvv_code                                      ## cvv code
        self.__card_balance = 0                                         ## card balance

    ## @brief
    # function for creating a random card number with a length of 16 characters
    # @return return card number
    def __create_random_card_number(self) -> str:
        random_card_number: str = ''
        for i in range(16):     ##required length 16 characters
            random_card_number += str(random.randint(0, 9))  ## using the random module, select a number and add it to the card number, changing it to a string simval.
        return random_card_number       ##returning the card number

    ##@brief
    # create a function for adding money to the card
    def add_money_to_card(self, add_money: float) -> None:
        self.__card_balance += add_money        ## adding money to the card

my_card = Card(000)