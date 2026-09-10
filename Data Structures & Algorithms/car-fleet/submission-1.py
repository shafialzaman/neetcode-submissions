class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        # print(pair)
# start in reverse order
        stk = []
        for p,s in pair:
            stk.append((target - p) / s) # d/r = t
            if len(stk) >= 2 and stk[-2] >= stk[-1]: # if furthest car takes longer than closest car
                stk.pop() # merge closest car
        return len(stk)