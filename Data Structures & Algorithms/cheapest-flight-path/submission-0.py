from _heapq import heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, c in flights:
            graph[s].append((d, c))

        heap = [(0, src, 0)]

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops + 1 > k +1:
                continue

            for neighbor, extraCost in graph[node]:
                heapq.heappush(heap, (cost + extraCost, neighbor, stops + 1))

        return -1

