class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        letterCount = {}

        for word in strs:
            wordSorted = "".join(sorted(word))
            if wordSorted in letterCount:
                letterCount[wordSorted].append(word)
            else:
                letterCount[wordSorted] = [word]
        
        for word in letterCount.keys():
            result.append(letterCount[word])

        return result
        