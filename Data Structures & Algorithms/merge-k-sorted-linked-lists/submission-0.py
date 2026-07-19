from _heapq import heappush
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst.val, i, lst))


        dummy = ListNode(0)
        curr = dummy

        while heap:
            lVal, i, lst = heapq.heappop(heap)

            curr.next = lst
            curr = curr.next

            if lst.next:
                heapq.heappush(heap, (lst.next.val, i, lst.next))

        return dummy.next