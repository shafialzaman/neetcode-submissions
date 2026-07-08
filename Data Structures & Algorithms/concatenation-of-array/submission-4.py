class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] * 2 * len(nums)
        print(ans)
        temp = []

        for i in nums:
            ans.append(i)
            temp.append(i)

        # print(ans)
        # print(temp)
        for j in nums:
            ans.append(temp.pop(0))
            # print(",",ans)

        # print(ans)
        # print(temp)
        

        return ans
        