class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needMap = {}
        for char in t:
            needMap[char] = needMap.get(char, 0) + 1

        l = 0
        need = len(t)
        bestSubLen = float('inf')
        best = ""
        for r in range(len(s)):
            rightChar = s[r]
            if rightChar in needMap and needMap[rightChar] > 0:
                need -= 1
            if rightChar in needMap:
                needMap[rightChar] -= 1
            while need == 0:
                if bestSubLen > (r - l) + 1:
                    best = s[l:r + 1]
                    bestSubLen = (r - l) + 1
                leftChar = s[l]
                
                if leftChar in needMap:
                    needMap[leftChar] += 1
                    if needMap[leftChar] > 0:
                        need += 1
                    
                l += 1

        return best
        