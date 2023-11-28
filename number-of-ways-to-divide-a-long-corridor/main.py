class Solution:
    def numberOfWays(self, corridor: str) -> int:
        parts = []

        t = 0
        for i, c in enumerate(corridor):
            if c == 'S':
                if t == 0:
                    start = i
                    t += 1
                else:
                    parts.append((start, i))
                    t = 0
            
        if t != 0 or len(parts) == 0:
            return 0

        result = 1
        for i in range(1, len(parts)):
            result *= (parts[i][0] - parts[i-1][1])
            result %= 10 ** 9 + 7

        return result
