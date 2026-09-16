class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])
        output = [intervals[0]]

        for a, b in intervals:
            lastend = output[-1][1]
            if a <= lastend:
                output[-1][1] = max(lastend,b)
            else:
                output.append([a,b])



        return output    
        