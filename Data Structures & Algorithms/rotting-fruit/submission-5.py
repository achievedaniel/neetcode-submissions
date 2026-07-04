class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        rotten = deque()

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append((r,c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
            
                for rr, rc in directions:
                    nr = rr + r
                    nc = rc + c

                    if nr >= 0 and nc >= 0 and nr < row and nc < col and grid[nr][nc] == 1:
                        rotten.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1

        