## @package transaction_type
#  @brief A model that represents transaction type in class transaction.

## @brief Using types to work with enum.
from enum import Enum

## @brief TransactionType
#  @details Transaction types allow you to understand the types of spending and crediting on your card so you can analyze your spending and income.
#  <br />TransactionType are inherited from class Transaction.
class TransactionType(Enum):
    ## @brief Type of expenses/income cash withdrawn and deposited at ATMs.
    сash = 1
    ## @brief Type of cash expenditures/income that occur online: shopping, paying by online transfer, receiving payment online, crediting payments, paying subscriptions and others.
    online_transfers = 2
    ## @brief Type of expenditures and revenues for goods.
    goods = 3
    ## @brief Type of expenses and income for services.
    services = 4