class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        biggestIsland = 0
        
        def islandSize(r, c):
            if r < 0 or c < 0 or r == row or c == col or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + islandSize(r + 1 ,c) + islandSize(r - 1 , c) + islandSize(r , c + 1) + islandSize(r , c - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    biggestIsland = max(biggestIsland, islandSize(r,c))

        return biggestIsland