import random
##@breaf
class Card:  # create a class
    __card_number: str  # create a parameter card number
    __card_owner: str   # create a parameter card owner
    __cvv_code: int   # create a parameter cvv code
    __card_balance: float   # create a parameter cardbalance

    ##@brief
    # @param [in] cvv_code Card CVV code
    # @param [in] card_owner Card Owner
    # @return return card number
    # @return return card balance
    def __init__(self, cvv_code, card_owner = 'Default') -> None:   ## create a function for adding money to the card
        self.__card_number = self.__create_random_card_number()   ## initialization of the card number parameter
        self.__card_owner = card_owner    ## initialization of the card owner parameter
        self.__cvv_code = cvv_code    ## cvv code
        self.__card_balance = 0    ## card balance

    ## @brief
    # @return return card number
    def __create_random_card_number(self) -> str:    ## function for creating a random card number with a length of 16 characters
        random_card_number: str = ''
        for i in range(16):     ## required length 16 characters
            random_card_number += str(random.randint(0, 9))     ## using the random module, select a number and add it to the card number, changing it to a string simval.
            return random_card_number    ## returning the card number

    ##@brief
    # @param [in] card_balance add money
    def add_money_to_card(self, add_money: float) -> None:    ## create a function for adding money to the card
        self.__card_balance += add_money        ## adding money to the card

my_card = Card(000)