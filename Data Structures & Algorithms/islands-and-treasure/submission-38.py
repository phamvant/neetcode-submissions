

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(r, c, count):
            grid[r][c]=min(grid[r][c], count)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != -1 and grid[nr][nc] > count:
                    bfs(nr, nc, count + 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i, j, 0)
