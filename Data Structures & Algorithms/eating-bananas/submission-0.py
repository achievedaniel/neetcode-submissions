class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            hoursNeeded = 0
            k = (l + r) // 2
            for num in piles:
                hoursNeeded += math.ceil(num / k)

            if hoursNeeded > h:
                l = k + 1
                
            else:
                r = k - 1
        return l
        