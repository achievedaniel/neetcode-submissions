# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        nxt = dummy

        while nxt.next:
            if nxt.next.val == val:
                nxt.next = nxt.next.next
            else:
                nxt = nxt.next

        return dummy.next



        