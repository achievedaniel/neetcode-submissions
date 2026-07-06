class Solution:
    def climbStairs(self, n: int) -> int:
        last = 0
        current = 1
        for _ in range(n):
            last, current = current, current + last

        return current
            

