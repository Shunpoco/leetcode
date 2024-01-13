class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo = defaultdict(int)

        for c1, c2 in zip(s, t):
            memo[c1] += 1
            memo[c2] -= 1


        plus, minus = 0, 0
        for _, v in memo.items():
            if v > 0:
                plus += v
            elif v < 0:
                minus -= v

        return max(plus, minus)
