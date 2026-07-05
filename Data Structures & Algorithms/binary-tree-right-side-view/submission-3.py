# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = deque()
        nodes.append(root)

        result = []

        if not root:
            return []

        while nodes:
            rightMost = len(nodes) -1

            for i in range(len(nodes)):
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                if i == rightMost:
                    result.append(node.val)

        return result