import unittest

from order_report import get_big_order_report


class BigOrderReportTests(unittest.TestCase):
    def test_counts_qualified_orders_and_converts_text_amounts(self):
        orders = [
            {"id": 1, "amount": 199, "user": "小王"},
            {"id": 2, "amount": "300", "user": "小李"},
            {"id": 3, "amount": 500, "user": "小张"},
        ]

        report = get_big_order_report(orders, minimum_amount=300)

        self.assertEqual(report["count"], 2)
        self.assertEqual(report["total"], 800.0)
        self.assertEqual(report["users"], ["小李", "小张"])
        self.assertEqual(report["invalid_order_ids"], [])

    def test_records_invalid_amounts(self):
        orders = [
            {"id": 4, "amount": None, "user": "小陈"},
            {"id": 5, "amount": "not-a-number", "user": "小赵"},
            {"id": 6, "amount": 300},
        ]

        report = get_big_order_report(orders, minimum_amount=300)

        self.assertEqual(report["count"], 1)
        self.assertEqual(report["total"], 300.0)
        self.assertEqual(report["users"], ["未知用户"])
        self.assertEqual(report["invalid_order_ids"], [4, 5])


if __name__ == "__main__":
    unittest.main()
