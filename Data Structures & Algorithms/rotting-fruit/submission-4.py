class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        dq = deque()
        row = len(grid)
        collumn = len(grid[0])
        for r in range(row):
            for c in range(collumn):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    dq.append((r,c))

        directions = [(0, -1),(0, +1),(-1, 0), (+1, 0)]
        while dq and fresh > 0:
            for _ in range(len(dq)):
                r, c = dq.popleft()

                for dr, dc in directions:
                    nr = dr +r
                    nc = dc + c

                    if 0 <= nr < row and 0 <= nc < collumn and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        dq.append((nr,nc))
            minutes += 1
            

        return minutes if fresh == 0 else -1



            