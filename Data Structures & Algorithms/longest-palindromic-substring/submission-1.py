class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r]
        
        res = ""
        for i in range(len(s)):
            lOdd = expand(i,i)
            lEven = expand(i,i +1)

            if len(lOdd) > len(lEven) and len(lOdd) > len(res):
                res = lOdd
            elif len(lEven) > len(res):
                res = lEven
        
        return res