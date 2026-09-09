class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        time = 0
        fresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh > 0:

            for i in range(len(q)):
                a,b = q.popleft()
                for dx, dy in dirs:
                    ax, by = a + dx, b + dy
                    if (0 <= ax < len(grid) and 0 <= by < len(grid[0]) and grid[ax][by] == 1):
                        grid[ax][by] = 2
                        q.append((ax,by))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1





            