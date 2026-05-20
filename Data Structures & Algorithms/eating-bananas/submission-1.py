class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) //2
            hourSum = sum(math.ceil(p/mid)  for p in piles)

            if hourSum > h:
                l = mid + 1
            else:
                r = mid - 1

        return l