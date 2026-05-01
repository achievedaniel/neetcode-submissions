class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        countSet = set(nums)
        longest = 1
        for num in countSet:
            if num - 1 not in countSet:
                current = num
                streak = 1

                while current + 1 in countSet:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest