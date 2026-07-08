class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] = hmap.get(i) + 1
        # print(hmap)

        temp = sorted(hmap.items(), key = lambda item : item[1])

        print(temp)
        ret = []
        for i in range(k):
            ret.append(temp.pop()[0])
        
        print(ret)
        return ret
