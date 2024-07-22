import heapq

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        q = []

        for name, height in zip(names, heights):
            heapq.heappush(q, (-height, name))

        result = []

        while len(q) > 0:
            result.append(heapq.heappop(q)[1])

        return result
