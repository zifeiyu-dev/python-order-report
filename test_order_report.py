import os
import unittest

from order_report import get_big_order_report, get_minimum_amount


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

    def test_uses_default_minimum_amount_when_not_configured(self):
        old_value = os.environ.pop("BIG_ORDER_MINIMUM", None)
        try:
            self.assertEqual(get_minimum_amount(), 300.0)
        finally:
            if old_value is not None:
                os.environ["BIG_ORDER_MINIMUM"] = old_value


if __name__ == "__main__":
    unittest.main()
