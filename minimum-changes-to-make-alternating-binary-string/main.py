class Solution:
    def minOperations(self, s: str) -> int:
        result = 0

        prev = '0'
        count = 0

        for c in s:
            if prev == c:
                count += 1
                if c == '0':
                    prev = '1'
                else:
                    prev = '0'
            else:
                prev = c

        result = count
        count = 0
        prev = '1'

        for c in s:
            if prev == c:
                count += 1
                if c == '0':
                    prev = '1'
                else:
                    prev = '0'
            else:
                prev = c

        return min(result, count)
