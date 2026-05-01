class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for n in range(len(nums)):

            if n > 0 and nums[n -1] == nums[n]:
                continue
            x, y = n + 1, len(nums) -1
            while x < y:
                numSum = nums[n] + nums[x] + nums[y]
                if numSum > 0:
                    y -= 1
                elif numSum < 0:
                    x += 1
                else:
                    result.append([nums[n], nums[x], nums[y]])
                    y -= 1
                    x += 1
                    while x < y and nums[x] == nums[x - 1]:
                        x += 1
        return result