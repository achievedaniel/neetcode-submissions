# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        index = 1
        indexNode = head
        while indexNode.next:
            index += 1
            indexNode = indexNode.next

        middle = math.ceil(index / 2)

        curr = head
        while middle > 1:
            curr = curr.next
            middle -= 1
        
        secondHead = curr.next
        curr.next = None

        reversedSecondHead = None
        while secondHead:
            nextNode = secondHead.next
            secondHead.next = reversedSecondHead
            reversedSecondHead = secondHead
            secondHead = nextNode

        firstHead = head
        while reversedSecondHead:
            tempNode = firstHead.next
            tempSecond = reversedSecondHead.next
            
            firstHead.next = reversedSecondHead
            reversedSecondHead.next = tempNode

            firstHead = tempNode
            reversedSecondHead = tempSecond