class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = nums[0]
        maxProd = nums[0]
        bestMax = nums[0]

        for num in nums[1:]:
            temp = minProd
            minProd = min(minProd * num, maxProd * num, num)
            maxProd = max(maxProd * num, temp * num, num)
            bestMax = max(bestMax, maxProd)

        return bestMax