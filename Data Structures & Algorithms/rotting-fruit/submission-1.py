class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        minutes = -1
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    dq.append((r,c))
        
        if fresh == 0:
            return 0

        direction = [(0,-1),(0,+1),(-1,0),(+1,0)]
        row = len(grid)
        column = len(grid[0])
        while dq:
            minutes += 1
            for _ in range(len(dq)):
                r , c = dq.popleft()
            

                for dr, dc in direction:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < row and 0 <= nc < column and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2 
                        dq.append((nr,nc))
        
        return minutes if fresh == 0 else -1

        