class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(n, pOpen, pClose, path):
            if n == pOpen and n == pClose:
                res.append(path)
                return

            if pOpen < n:
                dfs(n, pOpen + 1, pClose, path + "(")
            
            if pOpen > pClose:
                dfs(n, pOpen, pClose + 1, path + ")")
        dfs(n, 0, 0, "")
        return res
