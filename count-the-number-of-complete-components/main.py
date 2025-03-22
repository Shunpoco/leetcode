class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        result = 0
        visited = set()

        def dfs(cur: int, info: list) -> None:
            visited.add(cur)
            info[0] += 1
            info[1] += len(graph[cur])

            for nex in graph[cur]:
                if nex not in visited:
                    dfs(nex, info)

        for v in range(n):
            if v in visited:
                continue
            info = [0, 0]
            dfs(v, info)

            if info[0] * (info[0] - 1) == info[1]:
                result += 1

        return result

