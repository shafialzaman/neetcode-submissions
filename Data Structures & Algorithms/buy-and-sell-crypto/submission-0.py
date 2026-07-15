class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxim = 0

        for l in range(len(prices)):

            for r in range(l + 1, len(prices)):

                maxim = max(prices[r] - prices[l],maxim)
        
        return maxim

