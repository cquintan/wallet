import random


class Card:
    def __init__(self, cvv_code, card_owner = 'Default'):
        self.__card_number = self.__create_random_card_number()
        self.__card_owner = card_owner
        self.__cvv_code = cvv_code

    def __create_random_card_number(self):
        random_card_number = ''
        for i in range(16):
            random_card_number += str(random.randint(0, 9))
        return random_card_number
       
my_card = Card(000)