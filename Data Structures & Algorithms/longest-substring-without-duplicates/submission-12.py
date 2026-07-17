class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        b = 0
        if len(s) <= 1:
            return len(s)
        temp = ''
        maxstreak = 0
        # curmax = 0
        while a < len(s):
            curmax = 0
            b = a
            while b < len(s):
                val = s[b]
                if val in temp:
                    # print(val, curmax)
                    maxstreak = max(maxstreak,curmax)
                    # curmax
                    temp = ''
                    break                
                curmax += 1
                temp += val
                b += 1
                print(val,curmax,maxstreak,temp)

            maxstreak = max(maxstreak,curmax)
            # print(val,curmax,maxstreak)

            a += 1
        
        maxstreak = max(maxstreak,curmax)
        return maxstreak