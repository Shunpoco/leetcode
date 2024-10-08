class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        ub = 0

        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if len(stack) > 0:
                    stack.pop(-1)
                else:
                    ub += 1

        return (ub+1) // 2
