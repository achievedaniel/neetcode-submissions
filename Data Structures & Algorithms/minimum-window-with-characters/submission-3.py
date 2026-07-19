class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for c in t:
            count[c] = count.get(c, 0) +1
        
        need = len(t)
        res = ""
        resLen = float("inf")

        l = 0 

        for r in range(len(s)):

            if s[r] in count:
                if count[s[r]] > 0:
                    need -= 1
                count[s[r]] -= 1

            while need == 0:
                if (r - l + 1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                if s[l] in count:
                    if count[s[l]] >= 0:
                        need += 1
                    count[s[l]] += 1

                l += 1

        return res
