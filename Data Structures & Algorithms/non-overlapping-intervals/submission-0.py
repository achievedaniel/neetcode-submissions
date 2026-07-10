class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        newInt = []

        for s, e in intervals:
            if not newInt or newInt[-1][1] <= s:
                newInt.append([s,e])
            else:
                newInt[-1][1] = min(newInt[-1][1], e)
                res += 1

        return res