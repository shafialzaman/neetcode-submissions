class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.replace(" ", "")
        for v in t:
            if not v.isalpha() and not v.isnumeric():
                print(v)
                t = t.replace(v, "")
            if v.isupper():
                t = t.replace(v,v.lower())
        # print(t)
        i = 0
        j = len(t) - 1
        while i < j:
            # print(t[i],t[j])
            if t[i] != t[j]:
                return False
            i += 1
            j -= 1
        
        return True


