class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        while k > 0:
            c = self.count(n, cur, cur+1)

            if c <= k:
                k -= c
                cur += 1

            else:
                k -= 1
                cur *= 10

        return cur

    def count(self, n, p1, p2):
        c = 0

        while p1 <= n:
            c += min(p2, n+1) - p1
            p1 *= 10
            p2 *= 10

        return c
