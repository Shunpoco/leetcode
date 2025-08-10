class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nd = self.digits(n)
        p = 1
        d = self.digits(p)
        candidates = []
        while d <= nd:
            if d == nd:
                candidates.append(p)
            p *= 2
            d = self.digits(p)

        for c in candidates:
            if self.check(n, c):
                return True

        return False           

    def check(self, n, c):
        memo1 = defaultdict(int)
        while n > 0:
            memo1[n%10] += 1
            n //= 10

        memo2 = defaultdict(int)
        while c > 0:
            memo2[c%10] += 1
            c //= 10

        return memo1 == memo2

    def digits(self, n):
        r = 0
        while n > 0:
            r += 1
            n //= 10

        return r
