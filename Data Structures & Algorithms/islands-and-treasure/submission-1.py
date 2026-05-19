class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq = deque()
        row = len(grid)
        col = len(grid[0])

        for c in range(col):
            for r in range(row):
                if grid[r][c] == 0:
                    dq.append((r,c))

        directions = [(1,0),(-1,0),(0,-1),(0,1),]
        while dq:
            curr = dq.popleft()
            br = curr[0]
            bc = curr[1]

            for nr, nc in directions:
                r = br + nr
                c = bc + nc

                if r < 0 or c < 0 or r == row or c == col:
                    continue
                
                if grid[r][c] == 2147483647:
                    grid[r][c] = min(grid[r][c], grid[br][bc] + 1)
                    dq.append((r,c))

