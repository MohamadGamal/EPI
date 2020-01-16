def buy_sell_stock_once(A):
    previous_min = float('inf')
    max_profit = float('-inf')
    for s in A:
        previous_min = min(s, previous_min)
        max_profit = max(max_profit, s-previous_min)
    return max_profit


print(buy_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
