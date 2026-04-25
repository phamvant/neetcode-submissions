

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647
        
        def bfs(startR, startC):
            visited = set((startR, startC))
            q = deque([(startR, startC)])
            depth = 0

            while len(q) > 0:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    visited.add((r, c))

                    if grid[r][c] == -1:
                        continue;
                    
                    if grid[r][c] == 0:
                        print(r, c, depth)
                        return depth
                
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                            q.append((nr, nc))
                depth += 1

            return 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] > 0:
                    grid[i][j] = bfs(i, j)


            