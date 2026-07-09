class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        i = 0

        lst = [1] * len(nums)

        while i < len(nums):
            j = 0
            while j < len(nums):
                if i != j:
                    lst[i] *= nums[j]
                j += 1            
            i += 1
        
        return lst

        


