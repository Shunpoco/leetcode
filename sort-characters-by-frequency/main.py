class Solution:
    def frequencySort(self, s: str) -> str:
        memo = defaultdict(int)

        for c in s:
            memo[c] += 1

        v = [(v, k) for k, v in memo.items()]

        v.sort()

        r = []

        for i in range(len(v)-1, -1, -1):
            r.append(v[i][1]*v[i][0])

        return "".join(r)
