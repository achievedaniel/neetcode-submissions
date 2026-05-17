# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            leftSize = dfs(node.left)
            rightSize = dfs(node.right)

            if leftSize == -1 or rightSize == -1 or abs(leftSize - rightSize) > 1:
                return -1
            else:
                return 1 + max(leftSize, rightSize)

        return True if dfs(root) != -1 else False