class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, v = 0, len(s) - 1
        while i < v:
            while i < v and not s[i].isalnum():
                i += 1
            while i < v and not s[v].isalnum():
                v -= 1            
            if i < v:        
                if s[i].lower() == s[v].lower():
                    i += 1
                    v -= 1
                else:
                    return False

        return True

        