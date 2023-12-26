class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7

        memo = {}

        def solve(n, target):
            if memo.get((n, target)) is not None:
                return

            if n == 0 and target == 0:
                memo[(n, target)] = 1
                return

            if target < -1:
                memo[(n, target)] = 0
                return
            
            if n == 0:
                memo[(n, target)] = 0
                return

            result = 0
            for i in range(1, k+1):
                solve(n-1, target-i)
                result += memo[(n-1, target-i)]
                result %= mod

            memo[(n, target)] = result

        solve(n, target)

        return memo[(n, target)]
