class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  
        max_profit = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                max_profit = max(price, max_profit)
            
            else:
                l = r
            
        return max_profit



