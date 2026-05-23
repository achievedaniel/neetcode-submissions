class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        
        maxRight = height[r]
        maxLeft = height[l]

        water = 0

        while l <= r:
            if maxLeft > maxRight:
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
                r -= 1
            else:
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
                l += 1

        return water


        