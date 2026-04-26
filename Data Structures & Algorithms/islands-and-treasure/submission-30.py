

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647

        visited = set()
        q = deque()
        dist = 0

        def travel(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and grid[r][c] != -1 and grid[r][c] != 0:
                q.append((r, c))
                visited.add((r, c))
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        while len(q):
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                travel(r + 1, c)
                travel(r - 1, c)
                travel(r, c + 1)
                travel(r, c - 1)
                
            dist += 1

            