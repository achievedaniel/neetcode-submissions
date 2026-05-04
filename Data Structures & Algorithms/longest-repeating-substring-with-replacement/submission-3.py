class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_count = 0
        lettersCount = {}

        while r < len(s):
            lettersCount[s[r]] = lettersCount.get(s[r], 0) + 1
            max_count = max(max_count, lettersCount[s[r]])
            windowSize = (r - l) + 1
            if windowSize - max_count > k:
                lettersCount[s[l]] -= 1
                l += 1
        
            r += 1
        return r - l