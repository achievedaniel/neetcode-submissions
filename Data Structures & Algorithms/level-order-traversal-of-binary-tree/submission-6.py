# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        nodes.append(root)
        result = []

        if not root:
            return []

        while nodes:
            values = []
            for _ in range(len(nodes)):
                node = nodes.popleft()
                values.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            result.append(values)

        return result
