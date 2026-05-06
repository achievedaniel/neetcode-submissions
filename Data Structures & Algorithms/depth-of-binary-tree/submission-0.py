# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, count):
            if not node:
                return 0

            leftDepth = dfs(node.left, count + 1)
            rightDepth = dfs(node.right, count + 1)
            maxCount = max(leftDepth, rightDepth)

            return maxCount +1

        return dfs(root, 0)
    