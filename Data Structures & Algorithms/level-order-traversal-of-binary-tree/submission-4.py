# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque()
        res = []

        dq.append(root)

        while dq:
            size_level = len(dq)
            level = []
            for _ in range(size_level):
                curr = dq.popleft()
                level.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            res.append(level)
        return res


        