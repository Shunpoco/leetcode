from typing import List
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        memo = defaultdict(list)

        for road in roads:
            memo[road[0]].append(road[1])
            memo[road[1]].append(road[0])

        result = 0
        for i in range(n-1):
            for j in range(i+1, n):
                v = len(memo[i]) + len(memo[j])
                if i in memo[j]:
                    v -= 1

                if result < v:
                    result = v

        return result

