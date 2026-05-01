class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordsCount = {}
        if len(s) != len(t):
            return False
        for i, char in enumerate(s):
            if char in wordsCount:
                wordsCount[char] += 1
            else:
                wordsCount[char] = 1
        
        for i, char in enumerate(t):
            if char in wordsCount:
                wordsCount[char] -= 1
                if wordsCount[char] == 0:
                    wordsCount.pop(char)
            else:
                return False
        return True
        