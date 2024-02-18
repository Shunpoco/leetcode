import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        h1 = []
        h2 = []
        count = [0 for _ in range(n)]

        for i in range(n):
            heapq.heappush(h1, i)

        meetings.sort()
        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            while len(h2) > 0 and h2[0][0] <= start:
                v = heapq.heappop(h2)
                heapq.heappush(h1, v[1])

            if len(h1) > 0:
                room = heapq.heappop(h1)
                heapq.heappush(h2, (end, room))
            else:
                t, room = heapq.heappop(h2)
                heapq.heappush(h2, (t+end-start, room))

            count[room] += 1

        r = 0
        c = 0
        for i, v in enumerate(count):
            if v > c:
                r = i
                c = v

        return r
