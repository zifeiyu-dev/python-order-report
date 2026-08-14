# Python 订单分析器

创建并启用项目虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

看到命令行前出现 `(.venv)` 即表示已启用。退出虚拟环境使用 `deactivate`。

安装项目依赖：

```bash
python -m pip install -r requirements.txt
```

配置订单门槛（可选）：

```bash
export BIG_ORDER_MINIMUM=500
```

未设置时默认使用 300。真实 API Key 等敏感配置将放进 `.env`，不会提交到 Git。

运行命令：

```bash
python order_report.py
```

运行自动测试：

```bash
python -m unittest -v
```

请求一个公开 JSON 接口：

```bash
python fetch_todo.py
```

当前功能：从 `orders.json` 读取订单，清洗金额、筛选金额不少于 300 的订单，并输出统计报告。
