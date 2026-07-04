# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDepth(node):
            if not node:
                return 0

            leftMax = maxDepth(node.left)
            rightMax = maxDepth(node.right)

            return 1 + max(leftMax, rightMax)

        return maxDepth(root)
            
        