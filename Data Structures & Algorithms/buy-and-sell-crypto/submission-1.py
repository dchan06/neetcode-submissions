class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at the start look for the lowest price
        # at the end look for the highest price
        # two pointer
        l, r = 0, 1
        max_profit = 0
        while r < len(prices): 
            profit = prices[r] - prices[l]
            if profit > 0: 
                max_profit = max(profit, max_profit)
            else: 
                l = r
            r += 1
        return max_profit
            
