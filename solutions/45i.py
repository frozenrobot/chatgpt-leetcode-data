class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        # Initialize the buy and sell arrays
        buy = [float('-inf')] * 3
        sell = [0] * 3

        for price in prices:
            for i in range(1, 3):
                # Update the maximum profit achievable by buying at the current price
                # or not buying at all (using the maximum profit from the previous day)
                buy[i] = max(buy[i], sell[i - 1] - price)

                # Update the maximum profit achievable by selling at the current price
                # or not selling at all (using the maximum profit from the previous day)
                sell[i] = max(sell[i], buy[i] + price)

        # The maximum profit will be the maximum value in the sell array
        return sell[-1]
