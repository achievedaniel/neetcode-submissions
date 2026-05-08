# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        diameter = float('-inf')
        def dfs(node):
            nonlocal diameter    

            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            diameter = max(diameter, left + node.val + right)
            
            return node.val + max(left, right)
            
        
        dfs(root)
        return diameter

        