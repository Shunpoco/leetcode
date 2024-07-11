class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                t = []
                while len(stack) > 0 and stack[-1] != '(':
                    t.append(stack.pop(-1))
                stack.pop(-1)

                while len(t) > 0:
                    stack.append(t.pop(0))
            else:
                stack.append(c)

        return ''.join(stack)
