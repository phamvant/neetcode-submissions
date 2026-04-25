class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, size):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            
            # 2. VALUE CHECK SECOND (using integers, not strings)
            if grid[r][c] == 0:
                return 0

            # 3. SINK the land to avoid infinite loops
            grid[r][c] = 0

            grid[r][c] = 0
            maxSize =  1 + dfs(r + 1, c, size) + dfs(r - 1, c, size) + dfs(r, c + 1, size) + dfs(r, c - 1, size)
            return maxSize
            
        ret = 0

        for i in range(ROWS):
            for j in range(COLS):
                ret = max(ret, dfs(i, j, 0))
        
        return ret

