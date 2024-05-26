class Solution:
    def checkRecord(self, n: int) -> int:
        memo = {}

        self.calc(n, 0, 0, memo)

        return memo[(n, 0, 0)]

    def calc(self, n, a, l, memo):
        if memo.get((n, a, l)) is not None:
            return

        if n == 0:
            memo[(n, a, l)] = 1
            return

        r = 0
        # chose p
        self.calc(n-1, a, 0, memo)
        r += memo[(n-1, a, 0)]
        r %= (10**9 + 7)

        # chose a
        if a+1 < 2:
            self.calc(n-1, a+1, 0, memo)
            r += memo[(n-1, a+1, 0)]
            r %= (10**9 + 7)

        # chose l
        if l+1 < 3:
            self.calc(n-1, a, l+1, memo)
            r += memo[(n-1, a, l+1)]
            r %= (10**9 + 7)

        memo[(n, a, l)] = r

        return

