class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        maxWindow = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            maxFreq = max(maxFreq, count[s[r]])
            windowSize = r - l +1

            if windowSize - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            else:
                maxWindow = max(maxWindow, windowSize)

        return maxWindow

