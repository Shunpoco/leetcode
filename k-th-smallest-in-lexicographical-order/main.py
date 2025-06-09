class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        while k > 0:
            step = self.calc(n, cur, cur+1)

            if step <= k:
                cur += 1
                k -= step
            else:
                cur *= 10
                k -= 1

        return cur

    def calc(self, n, p1, p2):
        steps = 0

        while p1 <= n:
            steps += min(n+1, p2) - p1
            p1 *= 10
            p2 *= 10

        return steps
