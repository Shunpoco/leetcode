class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        self._tri(n, memo)

        return memo[n]

    def _tri(self, n, memo):
        if memo.get(n) is not None:
            return

        if n == 1 or n == 2:
            memo[n] = 1
            return

        if n == 0:
            memo[0] = 0
            return

        self._tri(n-3, memo)
        self._tri(n-2, memo)
        self._tri(n-1, memo)

        memo[n] = memo[n-3] + memo[n-2] + memo[n-1]

        return
