class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(pOpen, pClose, path):
            if pOpen == n and pClose == n:
                res.append(path)
                return

            if pOpen < n:
                dfs(pOpen + 1, pClose, path + "(")

            if pClose < pOpen:
                dfs(pOpen, pClose + 1, path + ")")

        dfs(0, 0, "")
        return res

