import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        q = []

        for i, s in enumerate(score):
            heapq.heappush(q, (-s, i))

        result = ["" for _ in range(len(score))]

        c = 0
        while len(q) > 0:
            c += 1
            v = heapq.heappop(q)

            if c == 1:
                result[v[1]] = "Gold Medal"
            elif c == 2:
                result[v[1]] = "Silver Medal"
            elif c == 3:
                result[v[1]] = "Bronze Medal"
            else:
                result[v[1]] = str(c)

        return result

