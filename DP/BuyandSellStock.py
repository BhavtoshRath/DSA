# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def BuySellStock1(prices):  # DP O(N^2)  - Brute Force
    maxProfit = 0
    for buy in range(0, len(prices)-1):
        for sell in range(buy+1, len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > maxProfit:
                maxProfit = profit
    return maxProfit

# prices = [7,1,5,3,6,4]
# prices = [4, 1, 5, 2, 7]
# max_profit = BuySellStock1(prices)
# print(max_profit)


def BuySellStock2(prices):  # DP O(N)  # Dynamic programing (Sliding window concept)
    maxProfit = 0
    buy_price = prices[0]
    for i in range(1, len(prices)):
        # Step1: Check if next price is less than buy price
        buy_price = min(buy_price, prices[i])
        # Step2: Calculate sell - buy
        potential_profit = prices[i] - buy_price
        # Step3: Find max of maxProfit and potential_profit
        maxProfit = max(maxProfit, potential_profit)
    return maxProfit


prices = [4, 3, 1, 5, 2, 7]
max_profit = BuySellStock2(prices)
print(max_profit)