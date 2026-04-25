class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit > 0:
                maxP = max(profit, maxP)
            else: 
                l = r

            r += 1

        return maxP