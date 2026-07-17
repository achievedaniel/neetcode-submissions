class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        def backtrack(i: int, cur: list):
            if i == len(s):
                res.append(cur[:])
                return
            for end in range(i, len(s)):
                if isPalindrome(s[i:end+1]):
                    cur.append(s[i:end+1])
                    backtrack(end +1, cur)
                    cur.pop()
        backtrack(0, [])
        return res

