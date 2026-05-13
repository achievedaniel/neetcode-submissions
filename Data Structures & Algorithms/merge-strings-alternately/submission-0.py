class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ""

        for c in range(min(len(word1), len(word2))):
            newWord += word1[c]
            newWord += word2[c]

        if len(word1) > len(word2):
            newWord += word1[len(word2):]
        
        if len(word2) > len(word1):
            newWord += word2[len(word1):]
        return newWord
        