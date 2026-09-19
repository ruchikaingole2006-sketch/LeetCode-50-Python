class Solution:
    def maxProfit(self, prices):
        minimum = float('inf')
        profit = 0

        for price in prices:
            minimum = min(minimum, price)
            profit = max(profit, price - minimum)

        return profit
