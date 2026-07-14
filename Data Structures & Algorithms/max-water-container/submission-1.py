class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxim = 0

        while l < r:
            temp0 = min(heights[l],heights[r])
            temp1 = (r - l) * temp0
            maxim = max(maxim,temp1)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxim
            