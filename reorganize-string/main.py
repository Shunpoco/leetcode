from collections import Counter

lass Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter()
        for c in s:
            counter[c] += 1

        q = []
        for k, v in counter.items():
            heapq.heappush(q, (-v, k))

        result = ""

        s = []
        while len(q) > 0:
            v = heapq.heappop(q)

            if len(result) > 0 and result[-1] == v[1]:
                if len(q) == 0:
                    return ""
                s.append(v)
                v = heapq.heappop(q)

            result += v[1]
            v = (v[0]+1, v[1])

            if v[0] != 0:
                heapq.heappush(q, v)

            while len(s) > 0:
                heapq.heappush(q, s.pop())


        return result

