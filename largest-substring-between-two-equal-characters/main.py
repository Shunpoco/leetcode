from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        memo = defaultdict(list)

        result = -1
        for i, c in enumerate(s):
            memo[c].append(i)
            if len(memo[c]) >= 2 and memo[c][-1] - memo[c][0] - 1 > result:
                result = memo[c][-1] - memo[c][0] - 1

        return result
