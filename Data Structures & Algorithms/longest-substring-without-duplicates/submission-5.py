class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxLen = 0
        visited = {}
        for r in range(len(s)):
            if s[r] in visited:
                l = max(visited[s[r]] + 1, l)
            visited[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
        return maxLen
            