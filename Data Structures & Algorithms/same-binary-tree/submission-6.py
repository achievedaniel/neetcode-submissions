# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (not node2 and node1):
                return False
            if node1.val != node2.val:
                return False

            l = dfs(node1.left, node2.left)
            r = dfs(node1.right, node2.right)
            return True if l and r else False
        
        if not p and not q:
            return True
        if not p and q or not q and p:
            return False
        if p.val == q.val:
            return dfs(p, q)
        else:
            return False

