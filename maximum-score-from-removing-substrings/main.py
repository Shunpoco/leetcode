class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pri = "ab" if x > y else "ba"
        low = "ab" if x <= y else "ba"

        result = 0
        s, v = self.calc(s, max(x, y), pri)
        result += v

        _, v = self.calc(s, min(x, y), low)
        result += v

        return result


    def calc(self, s, v, st):
        r = 0
        stack = []

        for c in s:
            if len(stack) > 0 and stack[-1]+c == st:
                r += v
                stack.pop(-1)
            else:
                stack.append(c)

        return (''.join(stack), r)
