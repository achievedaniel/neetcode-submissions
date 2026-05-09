class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = count.get(i, 0) + 1

        l = 0
        need = len(s1)

        for r in range(len(s2)):
            if s2[r] in count:
                if count[s2[r]] > 0:
                    need -= 1
                count[s2[r]] -= 1
                
            if r - l + 1 > len(s1):
                if s2[l] in count:
                    count[s2[l]] += 1
                    if count[s2[l]] > 0:
                        need += 1
                
                l += 1
 
            if need == 0:
                return True

        return False


        