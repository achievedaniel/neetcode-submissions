class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        maxNum = 0
        majority = 0

        for num in nums:
            numCount[num] = numCount.get(num, 0) +1
            if maxNum < numCount[num]:
                majority = num
            maxNum = max(maxNum, numCount[num])

        return majority

        
        