class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxim = 0

        for l in range(len(prices)):

            for r in range(l + 1, len(prices)):
                temp = prices[r] - prices[l]
                maxim = max(temp,maxim)
        
        return maxim

