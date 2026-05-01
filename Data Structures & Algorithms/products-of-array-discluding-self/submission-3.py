class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 0
        zeroCount = 0
        zeroPos = None

        for i, n in enumerate(nums):
            if n != 0:
                if product == 0:
                    product = 1
                product *= n
            else:
                zeroPos = i
                zeroCount += 1
        if zeroCount > 1:
            result = [0] * len(nums)
            return result
        if zeroPos != None and zeroCount == 1:
            result = [0] * len(nums)
            result[zeroPos] = product
            return result
        elif zeroCount == 0:
            result = [product] * len(nums)

        for x in range(len(result)):
            if nums[x] != 0:
                result[x] //= nums[x]

        return result