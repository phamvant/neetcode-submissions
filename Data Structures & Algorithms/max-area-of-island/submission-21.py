class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            # 1. BOUNDS CHECK FIRST
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            
            # 2. VALUE CHECK SECOND (using integers, not strings)
            if grid[r][c] == 0:
                return 0

            # 3. SINK the land to avoid infinite loops
            grid[r][c] = 0
            
            # 4. SUM result (1 for this cell + all 4 neighbors)
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1)) 
        ret = 0

        for i in range(ROWS):
            for j in range(COLS):
                ret = max(ret, dfs(i, j))
        
        return ret

