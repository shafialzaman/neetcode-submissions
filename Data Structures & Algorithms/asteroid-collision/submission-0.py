class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stk = []

        for i in asteroids:
            alive = True

            while stk and alive and stk[-1] > 0 and i < 0:
                if stk[-1] < abs(i):
                    stk.pop()

                elif stk[-1] == abs(i):
                    stk.pop()
                    alive = False
                else:
                    alive = False

            if alive: stk.append(i)
        # 2 4 
        # 2 
        return stk
