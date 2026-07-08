class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for i in strs:
            temp = ''.join(sorted(i))
            print(temp)
            map[temp].append(i)
        
        print(map)
        print(map.values())
        return list(map.values())