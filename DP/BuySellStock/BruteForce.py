# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def BuySellStock(prices):  # Brute force sliding window technique
    maxProfit = 0
    for buy in range(0, len(prices)-1):
        for sell in range(buy+1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > maxProfit:
                maxProfit = profit
    return maxProfit

# prices = [7,1,5,3,6,4]
prices = [4, 1, 5, 2, 7]
max_profit = BuySellStock(prices)
print(max_profit)