class Solution:
    def maxScore(self, s: str) -> int:
        c_zero = [0 for _ in range(len(s))]
        c_one = [0 for _ in range(len(s))]

        t = 0
        for i in range(len(s)):
            if s[i] == '0':
                t += 1
            c_zero[i] = t

        t = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                t += 1
            c_one[i] = t

        result = 0
        for i in range(len(s)-1):
            t = c_zero[i] + c_one[i+1]

            if t > result:
                result = t

        return result

