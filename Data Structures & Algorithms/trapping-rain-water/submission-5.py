class Solution:
    def trap(self, height: List[int]) -> int:
        waterTotal = 0
        l, r = 0, len(height) -1
        minL = height[l]
        minR = height[r]

        while l < r:
            if minL > minR:
                r -= 1
                wall = minR
                curWall = height[r]
                minR = max(minR, height[r])
                
            else:
                l += 1
                wall = minL
                curWall = height[l]
                minL = max(minL, height[l])
                
            water = wall - curWall
            if water > 0:
                waterTotal += water

        return waterTotal