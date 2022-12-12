class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*46
        memo[0] = 1

        return self._climb(n, memo)

    def _climb(self, n: int, memo: List[int]) -> int:
        if n < 0:
            return 0
        if memo[n] > 0:
            return memo[n]

        r = self._climb(n-1, memo) + self._climb(n-2, memo)

        memo[n] = r

        return r
