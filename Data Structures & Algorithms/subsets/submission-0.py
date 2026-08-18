class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        # res += 
        for num in nums:
            res += [[num] + j for j in res]
            print(num,res)
        
        return res