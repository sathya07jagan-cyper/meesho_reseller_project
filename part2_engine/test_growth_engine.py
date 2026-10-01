import unittest
from pathlib import Path

from part2_engine.growth_engine import mom_growth, is_flagged, validate_feed


class TestGrowthEngine(unittest.TestCase):

    def test_ethnic_wear_growth(self):
        growth = mom_growth(104520.77, 185107.61)
        self.assertEqual(growth, 77.1)
        self.assertEqual(is_flagged(growth), "flagged")

    def test_beauty_growth(self):
        growth = mom_growth(35542.11, 37559.07)
        self.assertEqual(growth, 5.67)
        self.assertEqual(is_flagged(growth), "not_flagged")

    def test_exact_boundary(self):
        growth = mom_growth(100000, 108000)
        self.assertEqual(growth, 8.0)
        self.assertEqual(
            is_flagged(growth), "escalate_exact_boundary"
        )

    def test_corrupted_feed(self):
        csv_path = Path(__file__).parent / "fixtures" / "corrupted_feed.csv"
        valid, errors = validate_feed(str(csv_path))

        self.assertFalse(valid)
        self.assertEqual(len(errors), 3)
        self.assertEqual(
            errors,
            [
                "line 3: negative revenue (-4200.0) for category=Western Wear",
                "line 4: missing category (month=July)",
                "line 6: missing revenue (category=Home & Kitchen)",
            ],
        )

    def test_valid_feed(self):
        csv_path = (
            Path(__file__).parent
            / "fixtures"
            / "monthly_category_revenue.csv"
        )
        valid, errors = validate_feed(str(csv_path))

        self.assertTrue(valid)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()