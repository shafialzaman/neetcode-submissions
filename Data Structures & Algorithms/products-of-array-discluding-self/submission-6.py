class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 0
        b = 0
        output = [1] * len(nums)
        print(output)
        while a < len(nums):
            prod = 1
            while b < len(nums):
                if a == b:
                    b += 1
                    continue
                prod *= nums[b]
                b += 1
            output[a] = prod
            a += 1
            b = 0
        return output
            


