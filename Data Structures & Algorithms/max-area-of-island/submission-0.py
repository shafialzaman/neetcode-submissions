class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        maxi = 0
        rows = len(grid)
        cols = len(grid[0])


        def bfs(x,y):

            q = deque()
            grid[x][y] = 0
            q.append((x,y))
            res = 1
            while q:

                ax,by = q.popleft()
                for dx,dy in dirs:
                    a, b = ax + dx, by + dy
                    if a < 0 or b < 0 or b >= cols or a >= rows or grid[a][b] == 0:
                        continue
                    q.append((a,b))
                    grid[a][b] = 0
                    res += 1
            
            return res

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxi = max(maxi,bfs(i,j))
        return maxi
                


        