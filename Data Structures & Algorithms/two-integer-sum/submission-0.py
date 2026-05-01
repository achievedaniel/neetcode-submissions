class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCount = {}

        for i, num in enumerate(nums):
            if target - num in numsCount:
                return [numsCount[target - num], i]
            numsCount[num] = i
                
        return[0,0]