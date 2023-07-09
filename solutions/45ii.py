class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        # Initialize the buy and sell variables
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            # Update the maximum profit achievable by buying at the current price
            # or not buying at all (using the maximum profit from the previous day)
            buy1 = max(buy1, -price)

            # Update the maximum profit achievable by selling at the current price
            # or not selling at all (using the maximum profit from the previous day)
            sell1 = max(sell1, buy1 + price)

            # Update the maximum profit achievable by buying at the current price
            # or not buying at all (using the maximum profit from the previous day)
            buy2 = max(buy2, sell1 - price)

            # Update the maximum profit achievable by selling at the current price
            # or not selling at all (using the maximum profit from the previous day)
            sell2 = max(sell2, buy2 + price)

        # The maximum profit will be the maximum value in the sell2 variable
        return sell2
