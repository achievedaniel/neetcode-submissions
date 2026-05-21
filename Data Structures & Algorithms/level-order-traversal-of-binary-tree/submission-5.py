# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = deque()
        dq.append(root)
        res = []

        while dq:
            path_len = len(dq)
            path = []

            for _ in range(path_len):
                curr = dq.popleft()
                path.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        
            res.append(path)

        return res

