import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        queue = []

        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                heapq.heappush(queue, (arr[i]/arr[j], arr[i], arr[j]))

        v = []
        for i in range(k):
            t = heapq.heappop(queue)
            v = [t[1], t[2]]

        return v

