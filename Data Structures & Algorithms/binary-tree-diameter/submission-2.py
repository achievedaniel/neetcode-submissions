# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]

        def dfs(node):
            if not node:
                return 0

            leftSize = dfs(node.left)
            rightSize = dfs(node.right)

            maxDiameter[0] = max(maxDiameter[0], leftSize + rightSize)
            
            return 1 + max(leftSize, rightSize)

        dfs(root)
        return maxDiameter[0]