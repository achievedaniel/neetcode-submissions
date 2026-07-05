# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def maxDiameter(node):
            if not node:
                return 0

            left = maxDiameter(node.left)
            right = maxDiameter(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        maxDiameter(root)

        return self.diameter
