"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        intervals.sort(key=lambda x: x.start)

        for i in intervals:
            if not minHeap or minHeap[0] > i.start:
                heapq.heappush(minHeap, i.end)
            else:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, i.end)
        
        return len(minHeap)

