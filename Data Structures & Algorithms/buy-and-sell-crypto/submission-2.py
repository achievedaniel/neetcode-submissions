class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPrice = 0

        while l < len(prices) - 1:
            maxPrice = max(maxPrice, prices[r] - prices[l])
            if prices[l] > prices[r] and r < len(prices) - 1:
                r += 1
                l += 1
            elif r < len(prices) - 1:
                r += 1
            else:
                l += 1
        return maxPrice
        