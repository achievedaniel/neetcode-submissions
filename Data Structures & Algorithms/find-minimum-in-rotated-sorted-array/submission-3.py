class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = float("inf")
        l, r = 0, len(nums) -1
        while l <= r:
            middle = (l + r) // 2
            if nums[l] > nums[middle]:
                minNum = min(nums[middle], minNum)
                r = middle -1
            else:
                minNum = min(nums[l], minNum)
                l = middle +1
                
        return minNum
            
        