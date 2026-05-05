class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        index = 1
        while curr.next:
            curr = curr.next
            index += 1

        if index == n:
            return head.next

        nodeToremove = head
        for _ in range(index - n - 1):
            nodeToremove = nodeToremove.next

        if nodeToremove.next:
            nodeToremove.next = nodeToremove.next.next
        
        return head