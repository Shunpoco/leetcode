class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)

        pairs = [(-q, q, 1) for q in quantities]

        heapq.heapify(pairs)

        for _ in range(n - m):
            ratio, total, stored_type = heapq.heappop(pairs)

            new_stored_type = stored_type + 1
            new_ratio = total / new_stored_type

            heapq.heappush(pairs, (-new_ratio, total, new_stored_type))

        _, total, stored_type = heapq.heappop(pairs)

        return math.ceil(total / stored_type)
