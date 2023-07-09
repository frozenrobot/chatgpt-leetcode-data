class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            # Update the first buy and sell variables
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)

            # Update the second buy and sell variables
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return sell2
