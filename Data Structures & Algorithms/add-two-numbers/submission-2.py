# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumed = ListNode()
        returnList = sumed
        carry = 0

        while l1 or l2 or carry:
            if l1 and l2:
                summedValue = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                summedValue = l1.val + carry
                l1 = l1.next
            elif l2:
                summedValue = l2.val + carry
                l2 = l2.next
            else:
                summedValue = carry

            sumed.val = summedValue % 10
            carry = summedValue // 10
            if l1 or l2 or carry:
                sumed.next = ListNode()
                sumed = sumed.next

        return returnList
