import random


class Card:
    __card_number: str
    __card_owner: str
    __cvv_code: int
    __card_balance: float

    def __init__(self, cvv_code, card_owner = 'Default') -> None:
        self.__card_number = self.__create_random_card_number()
        self.__card_owner = card_owner
        self.__cvv_code = cvv_code
        self.__card_balance = 0

    def __create_random_card_number(self) -> str:
        random_card_number: str = ''
        for i in range(16):
            random_card_number += str(random.randint(0, 9))
        return random_card_number
    def add_money_to_card(self, add_money: float) -> None:
        self.__card_balance += add_money

my_card = Card(000)