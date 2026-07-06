class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        current = 1
        for _ in range(n -1):
            last, current = current, current + last

        return current
            

