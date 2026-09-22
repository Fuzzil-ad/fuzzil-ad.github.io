import unittest

from DuckFine import DuckFine


class TestDuckFineInit(unittest.TestCase):
    def test_stores_member_id(self):
        fine = DuckFine("member-1")
        self.assertEqual(fine.member_id, "member-1")

    def test_starts_with_zero_owed(self):
        fine = DuckFine("member-1")
        self.assertEqual(fine.total_owed, 0.0)


class TestDuckFineCharge(unittest.TestCase):
    def setUp(self):
        self.fine = DuckFine("member-1")

    def test_negative_days_late_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.fine.charge(-1)

    def test_zero_days_late_is_free(self):
        self.assertEqual(self.fine.charge(0), 0.0)

    def test_days_within_grace_period_are_free(self):
        self.assertEqual(self.fine.charge(2), 0.0)

    def test_day_after_grace_period_is_charged(self):
        self.assertAlmostEqual(self.fine.charge(3), 0.50)

    def test_charge_scales_with_chargeable_days(self):
        self.assertAlmostEqual(self.fine.charge(6), 2.00)

    def test_deluxe_doubles_the_fee(self):
        self.assertAlmostEqual(self.fine.charge(4, deluxe=True), 2.00)

    def test_fee_is_capped_at_max_fee(self):
        self.assertEqual(self.fine.charge(100, deluxe=True), DuckFine.MAX_FEE)

    def test_charge_returns_the_fee_amount(self):
        fee = self.fine.charge(5)
        self.assertAlmostEqual(fee, 1.50)

    def test_total_owed_accumulates_across_charges(self):
        self.fine.charge(3)
        self.fine.charge(4)
        self.assertAlmostEqual(self.fine.total_owed, 1.50)


if __name__ == "__main__":
    unittest.main()
