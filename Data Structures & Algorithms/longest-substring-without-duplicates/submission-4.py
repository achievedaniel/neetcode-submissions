class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1
        maxLen = 1
        visited = {s[l]:l}
        while r <= len(s) -1 and l <= len(s) -2:
            if s[r] not in visited:
                visited[s[r]] = r
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                visited.pop(s[l])
                l += 1
        return maxLen
            