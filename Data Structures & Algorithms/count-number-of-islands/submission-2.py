class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        islandCount = 0

        def sinkIsland(r,c):
            if r < 0 or c < 0 or r == row or c == col:
                return
            
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            sinkIsland(r + 1, c)
            sinkIsland(r - 1, c)
            sinkIsland(r , c + 1)
            sinkIsland(r, c - 1)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    sinkIsland(r,c)
                    islandCount += 1
        

        return islandCount
        