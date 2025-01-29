class Solution:
    def findRedundantConnection(self, edges):
        N = len(edges)

        adj_list = [[] for _ in range(N)]

        for edge in edges:
            visited = [False] * N
            if self.isConnected(edge[0] - 1, edge[1] - 1, visited, adj_list):
                return edge

            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        return []

    def isConnected(self, src, target, visited, adj_list):
        visited[src] = True

        if src == target:
            return True

        result = False
        for adj in adj_list[src]:
            if not visited[adj]:
                result = result or self.isConnected(
                    adj, target, visited, adj_list
                )

        return result


