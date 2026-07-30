
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = max(piles)

        lo = 1
        hi = max(piles)
        
        while lo <= hi:
            k = (lo + hi) // 2
            hrs = 0
            
            for i in piles:
                hrs += math.ceil(float(i/k))

            if hrs <= h:
                res = min(res,k)
                hi = k - 1
            else:
                lo = k + 1

        
        return res
                
