class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # stk = []
        lst = []
        numb = 0
        # print(operations[-2])
        for i in operations:
            # print(lst)

            if i == '+':
                # print(lst[-1],lst[-2])
                temp = int(lst[-1]) + int(lst[-2])
                lst.append(temp)
            elif i == 'D':
                lst.append(int(lst[-1]) * 2)
            elif i == 'C':
                lst.pop()
            else:
                lst.append(int(i))
            print(lst)
        for j in lst:
            numb += int(j)

        return numb

