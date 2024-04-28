class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)

        count = [1 for _ in range(n)]
        result = [0 for _ in range(n)]

        def dfs(node=0, parent=None):
            for c in graph[node]:
                if c != parent:
                    dfs(c, node)
                    count[node] += count[c]
                    result[node] += result[c] + count[c]

        def dfs2(node=0, parent=None):
            for c in graph[node]:
                if c != parent:
                    result[c] = result[node] - count[c] + n - count[c]
                    dfs2(c, node)

        dfs()
        dfs2()

        return result

