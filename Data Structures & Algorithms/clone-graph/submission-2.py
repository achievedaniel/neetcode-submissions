"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if not node:
                return

            newNode = Node(node.val)
            visited[node] = newNode

            for n in node.neighbors:
                if n not in visited:
                    visited[node].neighbors.append(dfs(n))
                else:
                    visited[node].neighbors.append(visited[n])
                
            return newNode

        dfs(node)
        return visited[node] if visited else None

