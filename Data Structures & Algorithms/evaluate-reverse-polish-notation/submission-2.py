class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stk = []

        for i in tokens:
            temp = 0
            if i == '+':
                a,b = stk.pop(), stk.pop()
                stk.append(a+b)
            elif i == '-':
                a,b = stk.pop(), stk.pop()
                stk.append(b-a)

            elif i == '*':
                a,b = stk.pop(), stk.pop()
                stk.append(a*b)
                

            elif i == '/':
                a,b = stk.pop(), stk.pop()
                stk.append(int(b/a))

            else:
                stk.append(int(i))

            
        return stk[-1]
