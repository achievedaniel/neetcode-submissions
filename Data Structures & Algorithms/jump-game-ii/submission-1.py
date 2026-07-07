class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        window_end = 0
        farthest = 0

        for i in range(len(nums) -1):
            farthest = max(farthest, nums[i] + i)
            if i == window_end:
                jumps += 1
                window_end = farthest

        return jumps