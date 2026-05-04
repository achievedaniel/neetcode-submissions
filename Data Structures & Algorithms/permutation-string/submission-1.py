class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map = {}
        for l in s1:
            map[l] = map.get(l, 0) + 1
        l = 0
        needed = len(s1)
        for r in range(len(s2)):
            char = s2[r]
            if char in map:
                if map[char] > 0:
                    needed -= 1
                map[char] -= 1
                
            if r >= len(s1):
                left_char = s2[l]
                if left_char in map:
                    if map[left_char] >= 0:
                        needed += 1
                    map[left_char] += 1
                l += 1
            if needed == 0:
                return True
        return False