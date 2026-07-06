class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m -2, -1, -1):
            for r in range(n -2, -1, -1):
                row[r] += row[r +1]

        return row[0]