class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        degrees = [0 for _ in range(n)]

        for p in range(n):
            degrees[favorite[p]] += 1

        q = []
        for p in range(n):
            if degrees[p] == 0:
                q.append(p)

        depth = [1 for _ in range(n)]

        while len(q) > 0:
            cur = q.pop(0)
            nex = favorite[cur]

            depth[nex] = max(depth[nex], depth[cur]+1)
            degrees[nex] -= 1

            if degrees[nex] == 0:
                q.append(nex)

        longest_cycle = 0
        two_cycle = 0

        for p in range(n):
            if degrees[p] == 0:
                continue

            cycle_length = 0
            cur = p
            while degrees[cur] != 0:
                degrees[cur] = 0
                cycle_length += 1
                cur = favorite[cur]

            if cycle_length == 2:
                two_cycle += depth[p] + depth[favorite[p]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, two_cycle)
