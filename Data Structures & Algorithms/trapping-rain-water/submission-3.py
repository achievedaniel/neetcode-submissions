class Solution:
    def trap(self, height: List[int]) -> int:
        waterTotal = 0
        l, r = 1, len(height) -2
        minL = height[l -1]
        minR = height[r +1]

        while l <= r:
            if minL > minR:
                wall = minR
                curWall = height[r]
                minR = max(minR, height[r])
                r -= 1
            else:
                wall = minL
                curWall = height[l]
                minL = max(minL, height[l])
                l += 1
            water = wall - curWall
            if water > 0:
                waterTotal += water

        return waterTotal