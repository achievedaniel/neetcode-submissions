class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        res = []
        def backtrack(i, cur):
            if i == len(s):
                res.append(" ".join(cur))
                return

            
            for end in range(i, len(s)):
                if s[i:end+1] in wordSet:
                    cur.append(s[i:end +1])
                    backtrack(end + 1, cur)
                    cur.pop()

            
        backtrack(0, [])
        return res
