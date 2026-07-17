class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                l = stack.pop()
                temp = []
                while l != "[":
                    temp.append(l)
                    l = stack.pop()
                num_str = ""
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str

                num = int(num_str)
                temp.reverse()
                temp = ["".join(temp)] * num
                stack.append("".join(temp))

        return "".join(stack)

