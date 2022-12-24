from typing import List

class Solution:
    MOD = 1000000007
    def numTilings(self, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(3)] # all, only upper, only lower

        return self.exec(0, n, 0, memo)

    def exec(self, idx: int, n: int, f: int, memo: List[List[int]]) -> int:
        """
        f takes three values: 0 (all), 1 (only upper), and 2 (only lower)
        """
        if idx == n and f == 0:
            return 1
        elif idx > n or idx == n and f != 0:
            return 0

        if memo[f][idx] > 0:
            return memo[f][idx]

        r = 0
        if f == 0:
            # Put domino vertical
            r += self.exec(idx+1, n, 0, memo)
            r %= self.MOD
            # Put dominos horizontally
            r += self.exec(idx+2, n, 0, memo)
            r %= self.MOD
            # Put tromino upper side
            r += self.exec(idx+1, n, 2, memo)
            r %= self.MOD
            # Put tromino lower side
            r += self.exec(idx+1, n, 1, memo)
            r %= self.MOD
        elif f == 1:
            # Put domino
            r += self.exec(idx+1, n, 2, memo)
            r %= self.MOD
            # Put tromino lower side
            r += self.exec(idx+2, n, 0, memo)
            r %= self.MOD
        else:
            # Put domino
            r += self.exec(idx+1, n, 1, memo)
            r %= self.MOD
            # Put tromino upper side
            r += self.exec(idx+2, n, 0, memo)
            r %= self.MOD

        memo[f][idx] = r % self.MOD
        return r
