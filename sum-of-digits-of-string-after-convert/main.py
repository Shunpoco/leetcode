class Solution:
    def getLucky(self, s: str, k: int) -> int:
        q = []

        for c in s:
            q.append(ord(c)-ord('a')+1)


        for _ in range(k):
            t = 0
            for v in q:
                while v != 0:
                    t += v % 10
                    v //= 10

            q = [t]

        return q[0]
