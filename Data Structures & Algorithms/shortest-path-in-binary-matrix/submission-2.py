class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        EDGE = len(grid) -1

        directions = [(0, 1),(1, 0),(0, -1),(-1, 0),(1, 1),(1, -1),(-1, -1),(-1, 1)]
        
        q = deque()
        q.append((0,0))

        if grid[0][0] == 1:
            return -1
        
        grid[0][0] = 1

        while q:
            r, c = q.popleft()

            dist = grid[r][c]

            if r == EDGE and c == EDGE:
                return dist

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr <= EDGE and 0 <= nc <= EDGE and grid[nr][nc] == 0:
                    q.append((nr,nc))
                    grid[nr][nc] = dist + 1

        return -1


