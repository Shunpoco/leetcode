class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        q = []
        for interval in intervals:
            if len(q) == 0:
                heapq.heappush(q, interval[1])
            else:
                if q[0] < interval[0]:
                    v = heapq.heappop(q)
                heapq.heappush(q, interval[1])

        return len(q)
