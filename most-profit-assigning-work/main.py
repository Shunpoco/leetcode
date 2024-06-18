import heapq

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [(d, p) for d, p in zip(difficulty, profit)]
        jobs.sort()

        worker.sort()

        pq = []
        r = 0
        idx = 0
        for w in worker:
            while idx < len(jobs) and jobs[idx][0] <= w:
                heapq.heappush(pq, -jobs[idx][1])
                idx += 1

            if len(pq) > 0:
                r += -pq[0]

        return r

