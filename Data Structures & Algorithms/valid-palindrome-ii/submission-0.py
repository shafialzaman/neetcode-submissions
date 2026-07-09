class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(w: str) -> bool:
            t = w.replace(" ", "")
            for v in t:
                if not v.isalpha() and not v.isnumeric():
                    # print(v)
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
        
        for i in s:
            temp = s.replace(i,"")
            if isPalindrome(temp) == True:
                return True
        
        return False

        
        




    