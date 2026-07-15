class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # temp = sorted(set(nums))
        # nums[:len(temp)] = temp
        # return len(temp)

        k = 1 # 1 duplicate always

        for i in range(1,len(nums)):
            if nums[i] != nums[k-1]: # found non duplicate
                nums[k] = nums[i] # add non duplicate to next avail position
# 1 2 2 3 4
# 1 2 3 3 4

                k += 1

        del(nums[k:])

        print(nums)

        return k

