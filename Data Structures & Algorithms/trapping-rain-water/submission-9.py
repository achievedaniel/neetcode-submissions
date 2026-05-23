class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        
        maxRight = height[r]
        maxLeft = height[l]

        water = 0

        while l < r:
            if maxLeft > maxRight:
                r -= 1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
                
            else:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
                

        return water


        