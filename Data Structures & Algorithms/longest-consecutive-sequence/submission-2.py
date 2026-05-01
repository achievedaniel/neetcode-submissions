class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        countSet = set(nums)
        longCons = 1
        count = 1
        for num in nums:
            while num + 1 in countSet:
                count += 1
                num += 1
            longCons = max(longCons, count)
            count = 1

        return longCons