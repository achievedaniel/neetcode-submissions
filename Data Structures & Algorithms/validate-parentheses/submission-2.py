class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracktes = ['(','[','{']
        for p in s:
            if p in bracktes:
                stack.append(p)
            else:
                if not stack:
                    return False
                openB = stack.pop()
                if p == ')' and openB != '(':
                    return False
                elif p == ']' and openB != '[':
                    return False
                elif p == '}' and openB != '{':
                    return False
        return not stack