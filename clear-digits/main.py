class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            if c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                if len(stack) > 0:
                    stack.pop(-1)
            else:
                stack.append(c)

        return "".join(stack)
