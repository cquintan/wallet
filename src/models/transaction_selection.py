## @package transaction_selection
#  @brief A model that represents transaction selection in class transaction.

## @brief Using types to work with enum.
from enum import Enum

## @brief TransactionStatus
#  @details Transaction status allows to understand whether it was a credit or debit from the user's card.
#  <br />TransactionStatus are inherited from class Transaction.
class TransactionStatus(Enum):
    ## @brief Determining if it was an enrollment.
    enrollment = 1
    ## @brief Determining if it was a write-off.
    debiting = 2