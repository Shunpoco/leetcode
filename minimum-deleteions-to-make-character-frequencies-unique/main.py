class Solution:
    def minDeletions(self, s: str) -> int:
        counter = [0 for _ in range(26)]

        for c in s:
            counter[ord(c)-97] += 1

        m = max(counter)

        d = defaultdict(int)
        for v in counter:
            d[v] += 1

        r = 0

        for i in range(m, 0, -1):
            c = d[i]
            if c > 1:
                r += c-1
                d[i] = 1
                d[i-1] += c-1
        
        return r

