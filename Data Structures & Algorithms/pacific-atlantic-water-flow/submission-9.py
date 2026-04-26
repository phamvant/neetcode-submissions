class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        alt = set()
        pac = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        ROWS = len(heights)
        COLS = len(heights[0])

        for i in heights:
            print(i)

        def dfs(r, c, visited: set):
            if (r, c) in visited:
                return
                
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
        
        for i in range(COLS):
            dfs(0, i, pac)

        for i in range(COLS):
            dfs(ROWS - 1, i, alt)

        for i in range(ROWS):
            dfs(i, 0, pac)

        for i in range(ROWS):
            dfs(i, COLS - 1, alt)

        ret = []
        for (r, c) in alt:
            if (r, c) in pac:
                ret.append([r, c])

        return ret
            