from typing import List, Dict

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        self.exec(0, nums, n, memo)
        r = memo[0]
        return r


    def exec(self, b: int, nums: List[int], n: int, memo: Dict[int, int]):
        if memo.get(b) is not None:
            return

        cnt = bin(b).count("1")

        if cnt == n:
            memo[b] = 0
            return

        r = 0
        for i in range(n):
            bi = pow(2, i)
            if (b & bi) == bi:
                continue
            for j in range(i+1, n):
                bj = pow(2, j)
                if (b & bj) == bj:
                    continue

                t = self.gcd(nums[i], nums[j]) * (cnt//2+1)
                self.exec((b|bi|bj), nums, n, memo)
                t +=  memo[(b|bi|bj)]
                if r < t:
                    r = t

        memo[b] = r
        return

    def gcd(self, a: int, b: int) -> int:
        while b > 0:
            a, b = b, a%b

        return a

