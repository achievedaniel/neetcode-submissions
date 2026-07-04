# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def calculateDiameter(node):

            if not node:
                return 0

            maxLeft = calculateDiameter(node.left)
            maxRight = calculateDiameter(node.right)

            self.maxDiameter = max(self.maxDiameter, maxLeft + maxRight)

            return 1 + max(maxLeft, maxRight)

        calculateDiameter(root)

        return self.maxDiameter
