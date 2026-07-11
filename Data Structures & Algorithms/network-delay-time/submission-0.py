class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))

        heap = []
        heapq.heappush(heap, (0,k))
        visited = set()
        res = 0
        while heap:
            cost, node = heapq.heappop(heap)
            if node not in visited:
                visited.add(node)
                res = cost
                for neighbor, weight in graph[node]:
                    
                    heapq.heappush(heap, (cost + weight, neighbor))

        return res if len(visited) == n else -1








