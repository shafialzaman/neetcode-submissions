class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inc = defaultdict(int)
        out = defaultdict(int)

        for i,j in trust:
            inc[i] += 1
            out[j] += 1

        print(inc,out)
        
        temp = -1
        for b in out:
            if out[b] == n - 1:
                temp = b

        print(temp)
        if temp not in inc:
            return temp


        return -1
