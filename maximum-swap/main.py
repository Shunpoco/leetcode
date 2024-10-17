class Solution:
    def maximumSwap(self, num: int) -> int:
        ns = str(num)
        n = len(ns)

        seen = [-1] * 10

        for i in range(n):
            seen[int(ns[i])] = i

        for i in range(n):
            for d in range(9, int(ns[i]), -1):
                if seen[d] > i:
                    ns = list(ns)
                    ns[i], ns[seen[d]] = (ns[seen[d]], ns[i])
                    ns = "".join(ns)

                    return int(ns)

        return num
