class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        visited = set()




        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            peri = 0
            while q:
                x,y=q.popleft()
                for dx,dy in dirs:

                    nx,ny = x + dx , y + dy

                    if (nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] == 0):
                        peri += 1
                    elif (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny))
                
            return peri

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i,j)
        return 0


        