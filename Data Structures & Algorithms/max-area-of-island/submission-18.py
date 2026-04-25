class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            # 1. Bounds check FIRST, then value check
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0

            # 2. Mark as visited ('0') to avoid infinite loops
            grid[r][c] = 0
            
            # 3. Sum current cell + recursive neighbors
            # Note: you don't actually need the 'size' parameter in the function call
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            
        ret = 0

        for i in range(ROWS):
            for j in range(COLS):
                # Only start a DFS if we hit land
                if grid[i][j] == 1:
                    ret = max(ret, dfs(i, j))
        
        return ret