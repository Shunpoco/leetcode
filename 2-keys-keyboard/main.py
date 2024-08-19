class Solution:
    def minSteps(self, n: int) -> int:
        memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]

        self.calc(0, 1, n, memo)

        return memo[0][1]

    def calc(self, c, cur, n, memo):
        if cur > n:
            return -1
        if memo[c][cur] != -1:
            return memo[c][cur]


        if cur == n:
            memo[c][cur] = 0
            return 0

        r = float('inf')

        if c != cur:
            t = self.calc(cur, cur, n, memo)
            if t != -1:
                t += 1

                if r > t:
                    r = t

        if c > 0:
            t = self.calc(c, cur+c, n, memo)
            if t != -1:
                t += 1

                if r > t:
                    r = t

        if r == float('inf'):
            return -1

        memo[c][cur] = r
        return r
