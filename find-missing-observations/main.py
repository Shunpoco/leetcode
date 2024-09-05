class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sums = sum(rolls)

        rsum = mean * (n + len(rolls)) - sums

        if rsum > 6 * n or rsum < n:
            return []

        dmean = rsum // n
        mod = rsum % n

        elem = [dmean for _  in range(n)]

        for i in range(mod):
            elem[i] += 1

        return elem
