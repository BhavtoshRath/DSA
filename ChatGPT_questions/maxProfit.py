# You are given an array of integers representing a stock's prices over a certain period.
# Your task is to find the best time to buy and sell the stock to maximize your profit.
# You can only make one transaction (buy one and sell one share of the stock), and
# you cannot engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).


input_prices = [7, 1, 5, 3, 6, 4]
result = max_profit(input_prices)
print(result)  # Should output 5 (buy at 1, sell at 6 for a profit of 6 - 1 = 5)


# Find max(input_prices[i] - input_prices[j]), where i < j
def max_profit(input_prices):  # Brute force: o(N^2)
    ans = 0
    for i in range(len(input_prices) - 1):
        for j in range(i + 1, len(input_prices)):
            diff = input_prices[j] - input_prices[i]
            if diff > ans:
                ans = diff
    return ans


print(max_profit(input_prices))
