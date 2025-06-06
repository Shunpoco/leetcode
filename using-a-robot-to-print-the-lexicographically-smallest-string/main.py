class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        stack = []

        result = []

        minc = 'a'
        for c in s:
            stack.append(c)
            counter[c] -= 1
            while minc != 'z' and counter[minc] == 0:
                minc = chr(ord(minc)+1)
            while stack and stack[-1] <= minc:
                result.append(stack.pop())

        return "".join(result)

