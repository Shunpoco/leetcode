class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        memo = defaultdict(bool)

        return self.calc(0, s, memo)

    def calc(self, idx, s, memo) -> int:
        if idx == len(s):
            return 0

        result = 0
        for i in range(idx+1, len(s)+1):
            v = s[idx:i]

            if memo[v]:
                continue

            memo[v] = True
            t = 1 + self.calc(i, s, memo)
            if t > result:
                result = t
            memo[v] = False

        return result
