class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        memo = defaultdict(int)

        for n in arr:
            memo[n] += 1

        r = []
        for key, v in memo.items():
            r.append([v, key])

        r.sort()

        i = 0
        while k > 0:
            r[i][0] -= 1
            k -= 1
            if r[i][0] == 0:
                i += 1

        return len(r[i:])
