class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            lNum = heights[l]
            rNum = heights[r]
            maxArea = max(maxArea, (min(heights[l], heights[r]) * (r - l)))
            if lNum >= rNum:
                r -= 1
            else:
                l += 1
        return maxArea
        