class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total = 0
        length = len(nums) + 1

        while r < len(nums):
            total += nums[r]

            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1

            r += 1


        return length if length <= len(nums) else 0