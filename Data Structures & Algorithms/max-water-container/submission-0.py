class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = 0
        area = 0
        while a < len(heights):
            while b < len(heights):
                mini = min((heights[a]), heights[b])
                temp = (b - a) * mini
                print(a, b, 'heights',heights[a], heights[b],'area', temp)
                # print(heights[a])
                # print(temp)
                if temp > area:
                    area = temp
                b += 1
            a += 1
            b = a
        return area
        