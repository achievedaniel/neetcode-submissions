class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            l, r = 0, len(nums) - 1

            while l <= r:
                if nums[len(nums) - 1] < target:
                    break
        
                middle = (l + r) // 2
                if nums[middle] == target:
                    return True
                
                if nums[middle] > target:
                    r = middle - 1
                else:
                    l = middle + 1
        return False
                