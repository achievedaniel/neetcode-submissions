class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(i, path):
            if len(path) == len(digits):
                res.append(path)
                return

            for l in phone[digits[i]]:
                dfs(i +1, path + l)



        dfs(0, "")
        return res if digits else []
            



