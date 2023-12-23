class Solution:
    def maxScore(self, s: str) -> int:
        zeros = [0 for _ in range(len(s))]
        ones = [0 for _ in range(len(s))]

        for i, c in enumerate(s):
            if i != 0:
                zeros[i] = zeros[i-1]
            if c == '0':
                zeros[i] += 1

        for i in range(len(s)-1, -1, -1):
            if i != len(s)-1:
                ones[i] = ones[i+1]
            if s[i] == '1':
                ones[i] += 1

        result = 0
        for i in range(len(s)-1):
            t = zeros[i] + ones[i+1]
            if t > result:
                result = t

        return result
