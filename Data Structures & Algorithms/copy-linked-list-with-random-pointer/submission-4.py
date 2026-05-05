"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        def getNode(node: 'Optional[Node]'):

            if node is None:
                return None
            
            if node not in old_to_new:
                old_to_new[node] = Node(node.val)
            
            return old_to_new[node]
        
        curr = head

        while curr:
            copyNode = getNode(curr)
            copyNode.next = getNode(curr.next)
            copyNode.random = getNode(curr.random)
            curr = curr.next

        return old_to_new[head]