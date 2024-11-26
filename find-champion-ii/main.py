class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        memo = [0 for _ in range(n)]

        for edge in edges:
            memo[edge[1]] += 1

        result = -1
        c = 0
        for i, v in enumerate(memo):
            if v == 0:
                c += 1
                result = i

                if c > 1:
                    return -1

        if c != 1:
            return -1

        return result
