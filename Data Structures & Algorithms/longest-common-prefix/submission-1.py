class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            i = 0
            while i < len(word) and i < len(prefix) and word[i] == prefix[i]:
                    i += 1

            prefix = prefix[:i]
        
        return prefix