from enum import Enum

## @brief
#  create a transaction type class that determines whether the transaction is a credit or debit transaction
class TransactionStatus(Enum):
    crediting  = 1
    debiting = 2