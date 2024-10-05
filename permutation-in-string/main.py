class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        memo = defaultdict(int)
        for c in s1:
            memo[c] += 1

        start = 0

        while start + len(s1) <= len(s2):
            sub = s2[start:start+len(s1)]

            m = memo.copy()
            r = True
            for i, c in enumerate(sub):
                if m.get(c) is None or m[c] == 0:
                    start += 1
                    r = False
                    break
                m[c] -= 1

            if r:
                return True

        return False
