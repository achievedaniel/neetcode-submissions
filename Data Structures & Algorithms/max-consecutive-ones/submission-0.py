class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNums = 0
        countNums = 0
        for num in nums:
            if num == 1:
                countNums += 1
            else:
                countNums = 0
            maxNums = max(maxNums, countNums)
        return maxNums