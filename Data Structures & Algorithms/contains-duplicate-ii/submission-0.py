class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # 1 2 3 1 4

        for l in range(len(nums)):

            for r in range(l + 1, min(len(nums),l + 1 + k)):

                if nums[l] == nums[r]:
                    return True


        
        return False



