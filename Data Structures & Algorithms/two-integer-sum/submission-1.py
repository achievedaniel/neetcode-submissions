class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}

        for i, num in enumerate(nums):
            if target - num in remain:
                return [remain[target - num], i]
            remain[num] = i