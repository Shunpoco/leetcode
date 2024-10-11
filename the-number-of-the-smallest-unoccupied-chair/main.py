class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        q = []
        sheets = []
        for i in range(len(times)):
            heapq.heappush(sheets, i)

        times = [(t[0], t[1], i) for i, t in enumerate(times)]
        times.sort()

        for comer in times:
            now = comer[0]
            while len(q) > 0 and q[0][0] <= now:
                t = heapq.heappop(q)
                heapq.heappush(sheets, t[1])

            s = heapq.heappop(sheets)

            if comer[2] == targetFriend:
                return s

            heapq.heappush(q, (comer[1], s, comer[2]))

        return -1

 
