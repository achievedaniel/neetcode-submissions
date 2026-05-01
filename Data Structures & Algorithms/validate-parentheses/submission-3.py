class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracktes = {")": "(", "]": "[", "}": "{"}
        for p in s:
            if p not in bracktes:
                stack.append(p)
            else:
                if not stack:
                    return False
                openB = stack.pop()
                if openB != bracktes[p]:
                    return False
        return not stack