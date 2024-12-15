class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def _gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students

        pq = []

        for p, t in classes:
            gain = _gain(p, t)
            heapq.heappush(pq, (-gain, p, t))

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(pq)
            heapq.heappush(pq, (-_gain(p+1, t+1), p+1, t+1))

        result = 0
        while len(pq) > 0:
            _, p, t = heapq.heappop(pq)
            result += p / t

        return result / len(classes)
