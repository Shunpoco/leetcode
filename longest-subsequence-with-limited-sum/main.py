class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        answer = [-1 for _ in range(m)]

        sums = sum(nums)

        pq = []
        for num in nums:
            heapq.heappush(pq, -num)

        print(pq)

        for i, q in enumerate(queries):
            t = sums
            pq_ = pq.copy()

            while t > q:
                v = heapq.heappop(pq_)
                t -= -v

            answer[i] = len(pq_)

        return answer
