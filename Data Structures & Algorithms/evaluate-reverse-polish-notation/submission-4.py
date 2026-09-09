class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                x = stack.pop()
                y = stack.pop()

                if t == '+':
                    stack.append(x + y)
                elif t == '-':
                    stack.append(y - x)
                elif t == '*':
                    stack.append(x * y)
                else:
                    stack.append(int(y / x))

        return stack[0]


