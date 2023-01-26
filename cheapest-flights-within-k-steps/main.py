from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        paths = defaultdict(list)
        for flight in flights:
            paths[flight[0]].append((flight[1], flight[2]))

        default = 1000000000
        queue = [(src, 0, 0)]
        costs = [default for _ in range(n)]
        costs[src] = 0
        while len(queue) > 0:
            point = queue.pop(0)
            if point[2] > k:
                continue
            for transit in paths[point[0]]:
                if point[1]+transit[1] < costs[transit[0]]:
                    costs[transit[0]] = point[1]+transit[1]
                else:
                    continue
                if transit[0] != dst:
                    queue.append((transit[0], point[1]+transit[1], point[2]+1))
        
        if costs[dst] == default:
            return -1
        return costs[dst]

