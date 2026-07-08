class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ''
        for s in strs:
            for i in s:
                temp += i
                print(temp)
            temp += '-'
            # print(temp)
        return temp

        # just concatenate with _


    def decode(self, s: str) -> List[str]:
        curr = ''
        lst = []
        for i in s:
            if i == '-':
                lst.append(curr)
                curr = ''
            else:
                curr += i
        return lst


        # break down concat on _
