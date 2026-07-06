class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid) -1, len(obstacleGrid[0]) -1

        if obstacleGrid[0][0] == 1 or obstacleGrid[ROW][COL] == 1:
            return 0

        obstacleGrid[ROW][COL] = 1

        for r in range(ROW, -1, -1):
            for c in range(COL, -1, -1):
                
                if r == ROW and c == COL:
                    continue

                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0

                else:
                    down = obstacleGrid[r +1][c] if r +1 <= ROW else 0
                    right = obstacleGrid[r][c +1] if c +1 <= COL else 0
                    obstacleGrid[r][c] = down + right

        return obstacleGrid[0][0]
                