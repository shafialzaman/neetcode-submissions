class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        streak = 1
        maxstreak = 1

        a = 0

        nums.sort()
        while a < len(nums):
            streak = 1
            prev = nums[a]
            b = a + 1
            while b < len(nums):
                right = nums[b]
                if right == prev + 1:
                    streak += 1
                    prev = right

                elif right == prev:
                    pass
                else:
                    break
                b += 1
            maxstreak = max(maxstreak,streak)

            a = b
        return maxstreak