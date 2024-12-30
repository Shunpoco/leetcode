class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        memo = [0 for _ in range(high+1)]
        memo[0] = 1

        MOD = 10 ** 9 + 7

        for i in range(1, high+1):
            if i >= zero:
                memo[i] += memo[i-zero]

            if i >= one:
                memo[i] += memo[i-one]

            memo[i] %= MOD

        return sum(memo[low:high+1]) % MOD

