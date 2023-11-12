from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stops = defaultdict(list) # bus stops to bus lines
        max_stop = -1
        for i, route in enumerate(routes):
            for r in route:
                stops[r].append(i)
                if r > max_stop:
                    max_stop = r

        if max_stop < source or max_stop < target:
            return -1

        visited_stop = [float('inf') for _ in range(max_stop+1)]
        visited_stop[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, visited_stop[stop])
                mini += 1
                for stop in route:
                    if visited_stop[stop] > mini:
                        visited_stop[stop] = mini
                        flag = True

        return visited_stop[target] if visited_stop[target] < float('inf') else -1
