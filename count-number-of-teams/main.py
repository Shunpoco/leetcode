class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        mins = [[] for _ in range(n)]
        maxs = [[] for _ in range(n)]

        for i in range(n-1, -1, -1):
            v = rating[i]
            for j in range(i+1, n):
                if v > rating[j]:
                    maxs[i].append(j)
                else:
                    mins[i].append(j)

        result = 0

        for i in range(n):
            # mins
            for j in mins[i]:
                result += len(mins[j])

            # maxs
            for j in maxs[i]:
                result += len(maxs[j])

        return result

