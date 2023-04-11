from functools import reduce

class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        
        stack = []

        for i in range(n):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop(-1)

        result = reduce(lambda a, b: a+b, stack, '')

        return result
