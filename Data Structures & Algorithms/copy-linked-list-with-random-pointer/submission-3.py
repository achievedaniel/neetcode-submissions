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
        added = {}

        newHead = Node(0)
        newCurr = newHead
        curr = head
        while curr:

            if curr not in added:
                newCurr.next = Node(curr.val)
                added[curr] = newCurr.next

                newCurr = newCurr.next
                curr = curr.next

        copyHead = newHead.next
        curr = head

        while copyHead:
            if curr.random:
                copyHead.random = added[curr.random]
            copyHead = copyHead.next
            curr = curr.next

        return newHead.next