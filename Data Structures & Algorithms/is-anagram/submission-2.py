class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordsCount = {}
        if len(s) != len(t):
            return False
        for (char, char1) in zip(s, t):
            if char in wordsCount:
                wordsCount[char] += 1
                if wordsCount[char] == 0:
                    wordsCount.pop(char)
            else:
                wordsCount[char] = 1
            if char1 in wordsCount:
                wordsCount[char1] -= 1
                if wordsCount[char1] == 0:
                    wordsCount.pop(char1)
            else:
                wordsCount[char1] = -1

        return wordsCount == {}
        