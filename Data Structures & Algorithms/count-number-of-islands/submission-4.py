class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r == ROWS or c == COLS or grid[r][c] == '0' or c < 0 or r < 0:
                return

            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def sink(r, c):
            if r == ROWS or c == COLS or grid[r][c] == '0' or c < 0 or r < 0:
                return False
            
            dfs(r, c)
            print(grid)
            return True
        
        ret = 0

        for i in range(ROWS):
            for j in range(COLS):
                if sink(i, j):
                    ret += 1
        
        return ret

