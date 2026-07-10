class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (s, e) in enumerate(intervals):
            ns, ne = newInterval[0], newInterval[1]
            if e < ns:
                res.append([s,e])
            elif s > ne:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(ns, s), max(ne, e)]
        res.append(newInterval)
        return res


