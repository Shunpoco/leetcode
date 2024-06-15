import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(c, p) for c, p in zip(capital, profits)]
        projects.sort()

        hq = []

        i = 0
        while k > 0:
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(hq, -projects[i][1])
                i += 1

            if len(hq) == 0:
                break
            p = heapq.heappop(hq)
            w += -p
            k -= 1

        return w

