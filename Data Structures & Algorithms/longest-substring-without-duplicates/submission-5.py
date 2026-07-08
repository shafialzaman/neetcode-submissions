class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1
        maxval = 0
        curmax = 0
        a = 0
        b = 0
        temp = ''
        while a < len(s):


            while b < len(s):
                val = s[b]
                if val in temp:
                    print(val, curmax)
                    maxval = max(maxval,curmax)
                    temp = ''
                    curmax = 0
                    break
                else:
                    curmax += 1
                    temp += val
                    b += 1


            
            a += 1
            b = a
        return maxval

            