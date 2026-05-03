class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ("+", "*", "-", "/"):
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                match token:
                    case "+":
                        stack.append(left + right)
                    case "-":
                        stack.append(left - right)
                    case "*":
                        stack.append(left * right)
                    case "/":
                        stack.append(int(left / right))
        return stack[0]
