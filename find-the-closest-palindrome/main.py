class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)

        i = l // 2 - 1 if l % 2 == 0 else l // 2

        fh = int(n[:i+1])

        pos = []

        pos.append(self.halfToPalindrome(fh, l%2==0))
        pos.append(self.halfToPalindrome(fh+1, l%2==0))
        pos.append(self.halfToPalindrome(fh-1, l%2==0))
        pos.append(10**(l-1)-1)
        pos.append(10**l+1)

        diff = float('inf')
        res = 0
        nl = int(n)

        for p in pos:
            if p == nl:
                continue
            if abs(p-nl) < diff:
                diff = abs(p-nl)
                res = p
            elif abs(p-nl) == diff:
                res = min(res, p)

        return str(res)

    def halfToPalindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left = left // 10
        while left > 0:
            res = res * 10 + left % 10
            left //= 10

        return res
