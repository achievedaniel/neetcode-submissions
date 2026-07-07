class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2, = text2, text1

        dp = [0] * (len(text2) + 1)

        for r in range(len(text1) -1, -1 , -1):
            diagnonal = 0
            for c in range(len(text2) -1, -1, -1):
                tempDiagonal = dp[c]
                if text1[r] == text2[c]:
                    dp[c] = 1 + diagnonal
                else:
                    dp[c] = max(dp[c], dp[c +1])
                diagnonal = tempDiagonal

        return dp[0]
