
class Solution:
    def soupServings(self, n: int) -> float:
        if n % 25 != 0:
            n = n // 25 + 1
        else:
            n //= 25

        if n >= 200:
            return 1.0

        memo = [[-1.0 for _ in range(n+1)] for _ in range(n+1)]
        memo[0][0] = 0.5
        for i in range(1, n+1):
            memo[0][i] = 1.0
            memo[i][0] = 0.0

        self.calc(n, n, memo)

        return memo[n][n]

    def calc(self, a, b, memo):
        if memo[a][b] >= 0.0:
            return

        v = 0.0
        if a == 0 and b == 0:
            v = 0.0
        elif a == 0:
            v = 1.0
        elif b == 0:
            v = 0.0
        else:
            for da, db in [(4, 0), (3, 1), (2, 2), (1, 3)]:
                a1 = max(0, a-da)
                b1 = max(0, b-db)
                self.calc(a1, b1, memo)

                v += 0.25 * memo[a1][b1]

        memo[a][b] = v


