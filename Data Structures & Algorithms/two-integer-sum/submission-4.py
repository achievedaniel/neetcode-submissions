class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iMap = {}

        for i, num in enumerate(nums):
            if target - num in iMap:
                return [iMap[target - num], i]
            else:
                iMap[num] = i

