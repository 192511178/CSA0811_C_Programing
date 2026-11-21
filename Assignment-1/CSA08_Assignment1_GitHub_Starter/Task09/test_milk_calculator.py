import unittest
from decimal import Decimal
from milk_calculator import rate_per_litre, payout, ten_day_total

class MilkCalculatorTests(unittest.TestCase):
    def test_reference_rate(self):
        self.assertEqual(rate_per_litre("3.5", "8.5"), Decimal("30.00"))

    def test_expected_examples(self):
        self.assertEqual(payout("8.5", "4.2", "8.7"), Decimal("283.90"))
        self.assertEqual(payout("12", "3.1", "8.3"), Decimal("333.60"))

    def test_negative_litres_rejected(self):
        with self.assertRaises(ValueError):
            payout("-1", "3.5", "8.5")

    def test_fat_out_of_range_rejected(self):
        with self.assertRaises(ValueError):
            payout("10", "7.1", "8.5")

    def test_total(self):
        entries = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7")]
        self.assertEqual(ten_day_total(entries), Decimal("583.90"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
