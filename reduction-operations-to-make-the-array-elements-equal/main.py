from typing import List
import heapq

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        for num in nums:
            memo[num] += 1

        q = []
        for num, count in memo.items():
            heapq.heappush(q, (-num, count))

        result = 0
        while len(q) > 1:
            _, lc = heapq.heappop(q)
            sv, sc = heapq.heappop(q)

            sc += lc
            result += lc
            heapq.heappush(q, (sv, sc))

        return result

