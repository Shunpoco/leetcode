class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7

        memo = {}
        def dp(p: int, s: int):
            if memo.get((p, s)) is not None:
                return

            if p == 0 and s == 0:
                memo[(p, s)] = 1
                return
            if s == 0:
                memo[(p, s)] = 0
                return

            dp(p, s-1)
            v = memo[(p, s-1)]
            if p > 0:
                dp(p-1, s-1)
                v += memo[(p-1, s-1)]
                v %= mod
            if p < arrLen-1:
                dp(p+1, s-1)
                v += memo[(p+1, s-1)]
                v %= mod

            memo[(p, s)] = v

        dp(0, steps)

        return memo[(0, steps)]

