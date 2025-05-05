class Solution:
    MOD = 10 ** 9 + 7

    def numTilings(self, n: int) -> int:

        memo = {}

        self.calc(0, 0, n, memo)

        return memo[(0, 0)]

    def calc(self, first, second, n, memo):
        if memo.get((first, second)):
            return

        if first > n or second > n:
            memo[(first, second)] = 0
            return

        if first == second and first == n:
            memo[(first, second)] = 1
            return

        result = 0

        if first == second:
            # 1. domino horizontally
            self.calc(first+2, second+2, n, memo)

            result += memo[(first+2, second+2)]
            result %= self.MOD

            # 2. Put domino vertically
            self.calc(first+1, second+1, n, memo)

            result += memo[(first+1, second+1)]
            result %= self.MOD

            # 3. Put Tromino
            self.calc(first+2, second+1, n, memo)
            self.calc(first+1, second+2, n, memo)

            result += memo[(first+2, second+1)]
            result %= self.MOD

            result += memo[(first+1, second+2)]
            result %= self.MOD

        elif first == second+1:
            # 1. Put domino
            self.calc(first, second+2, n, memo)
            result += memo[(first, second+2)]
            result %= self.MOD

            # 2. Put Tromino
            self.calc(first+1, second+2, n, memo)
            result += memo[(first+1, second+2)]
            result %= self.MOD

        elif first+1 == second:
            # 1. Put domino
            self.calc(first+2, second, n, memo)
            result += memo[(first+2, second)]
            result %= self.MOD

            # 2. Put Tromino
            self.calc(first+2, second+1, n, memo)
            result += memo[(first+2, second+1)]
            result %= self.MOD

        memo[(first, second)] = result

        return

