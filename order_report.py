import json


def load_orders(file_path):
    """从 JSON 文件读取订单列表。"""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_big_order_report(orders, minimum_amount=200):
    """返回大额订单的统计报告，并记录无法识别金额的订单编号。"""
    count = 0
    total = 0
    users = []
    invalid_order_ids = []

    for order in orders:
        try:
            amount = float(order.get("amount"))
        except (TypeError, ValueError):
            invalid_order_ids.append(order.get("id", "未知编号"))
            continue

        if amount >= minimum_amount:
            count += 1
            total += amount
            users.append(order.get("user", "未知用户"))

    return {
        "count": count,
        "total": total,
        "users": users,
        "invalid_order_ids": invalid_order_ids,
    }


if __name__ == "__main__":
    orders = load_orders("orders.json")
    report = get_big_order_report(orders, minimum_amount=300)

    print("大额订单报告")
    print(f"数量：{report['count']}")
    print(f"总金额：{report['total']:.2f}")
    print(f"用户：{', '.join(report['users'])}")
    print(f"无效订单编号：{report['invalid_order_ids']}")
