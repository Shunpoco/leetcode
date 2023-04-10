class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        stack = []

        for c in s:
            if pairs.get(c) is not None:
                if len(stack) > 0 and stack[-1] == pairs[c]:
                    stack.pop()

                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
