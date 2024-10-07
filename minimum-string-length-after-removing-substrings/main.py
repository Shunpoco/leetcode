class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            if len(stack) > 0 and (stack[-1]+c == "AB" or stack[-1]+c == "CD"):
                stack.pop(-1)
            else:
                stack.append(c)

        return len(stack)

