class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 , dp2 = 1, 0
        
        for i in range(len(s) -1, -1, -1):
            res = 0
            if 1 <= int(s[i]) <= 9:
                res += dp1
            if i +1 < len(s) and 10 <= int(s[i]+ s[i +1]) <= 26:
                res += dp2
            dp1, dp2 = res, dp1
        return dp1


 