# 定义需要的变量
name = "格力电器"
stock_price = 31.11
# 股票 价格 每日 增长 因子
stock_price_daily_growth_factor = 1.2
stock_code = "000651"
growth_days = 7
finally_stock1_price = stock_price * growth_days * stock_price_daily_growth_factor

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数：%.1f，如果经过%d天的稳定增长后，股价将会达到：%.2f" % (stock_price_daily_growth_factor, growth_days, finally_stock1_price))