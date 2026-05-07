# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {value: index for index, value in enumerate(inorder)}
        idx = 0
        def dfs(left, right):
            nonlocal preorder
            nonlocal indexMap
            nonlocal idx

            if left > right:
                return

            value = preorder[idx]

            node = TreeNode(value)
            
            mid = indexMap[value]

            idx += 1

            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)
            return node

        return dfs(0, len(inorder) -1)
