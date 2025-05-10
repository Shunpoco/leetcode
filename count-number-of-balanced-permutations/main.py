class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10 ** 9 + 7

        num = list(map(int, num))
        total = sum(num)

        if total % 2 != 0:
            return 0

        target = total // 2
        count = Counter(num)

        n = len(num)

        mOdd = (n+1) // 2

        psum = [0] * 11
        for i in range(9, -1, -1):
            psum[i] = psum[i+1] + count[i]

        @cache
        def dfs(pos, cur, oddCount):
            if oddCount < 0 or psum[pos] < oddCount or cur > target:
                return 0
            if pos > 9:
                return int(cur == target and oddCount == 0)

            evenCount = psum[pos] - oddCount
            res = 0
            for i in range(max(0, count[pos]-evenCount), min(count[pos], oddCount)+1):
                ways = comb(oddCount, i) * comb(evenCount, count[pos]-i) % MOD
                res += ways * dfs(pos+1, cur+i*pos, oddCount-i)
            return res % MOD

        return dfs(0, 0, mOdd)
