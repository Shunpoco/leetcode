class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        counter = [0 for _ in range(n+1)]

        for edge in edges:
            counter[edge[0]] += 1
            if counter[edge[0]] == n-1:
                return edge[0]

            counter[edge[1]] += 1
            if counter[edge[1]] == n-1:
                return edge[1]

        # Unreachable
        return 0


