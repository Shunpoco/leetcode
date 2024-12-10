class Solution:
    def maximumLength(self, s: str) -> int:
        memo = {}

        for i in range(len(s)):
            c = s[i]
            l = 0

            for j in range(i, len(s)):
                if c == s[j]:
                    l += 1
                    memo[(c, l)] = memo.get((c, l), 0) + 1
                else:
                    break

        result = 0
        for i in memo.items():
            l = i[0][1]
            if i[1] >= 3 and l > result:
                result = l

        if result == 0:
            return -1

        return result

