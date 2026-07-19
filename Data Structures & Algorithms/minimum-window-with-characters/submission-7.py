class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sc = {}

        for c in t:
            sc[c] = sc.get(c, 0) +1

        resLen = float("inf")
        res = ""
        need = len(t)
        l = 0

        for r in range(len(s)):

            if s[r] in sc:
                if sc[s[r]] > 0:
                    need -= 1

                sc[s[r]] -= 1

            while need == 0:
                if r - l + 1 < resLen:
                    res = s[l:r +1]
                    resLen = r - l + 1
                
                if s[l] in sc:
                    if sc[s[l]] >= 0:
                        need += 1
                    sc[s[l]] += 1
                
                l += 1
        return res
