class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        hi = len(nums) - 1
        lo = 0

        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        if nums[mid] > target:
            return mid
        return mid + 1