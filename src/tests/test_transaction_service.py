import unittest
import datetime
from context import models
from context import services

class TestTransactionService(unittest.TestCase):
    def test_add_transaction(self):
        sample_card_number = "2200 1100 3300 4400"
        sample_transaction_status = models.TransactionStatus.enrollment
        sample_transaction_amount = 100
        sample_transaction_date_time = datetime.datetime.now()
        
        sample_transaction = models.Transaction(card_number=sample_card_number, card_transaction=sample_transaction_status, transaction_amount=sample_transaction_amount, transaction_date_time=sample_transaction_date_time)
        
        sample_transaction_service = services.TransactionService()
        self.assertTrue(sample_transaction_service.add_transaction(sample_transaction))

if __name__ == "__main__":
    unittest.main()