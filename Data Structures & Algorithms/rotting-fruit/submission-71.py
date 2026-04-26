class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647

        visited = set()
        q = deque()
        time = 0
        fresh = 0
        rot = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
        
        if fresh == 0:
            return 0

        while len(q):
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] != 2 and grid[nr][nc] != 0:
                        q.append((nr, nc))
                        visited.add((nr, nc))

            time += 1

        return time - 1 if fresh == 0 else -1
        

            