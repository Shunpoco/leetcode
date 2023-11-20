class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        
        memo = {
            'G': [[0, 0] for _ in range(n)],
            'P': [[0, 0] for _ in range(n)],
            'M': [[0, 0] for _ in range(n)],
        }

        for i in range(n-1, -1, -1):
            if i != n-1:
                memo['G'][i][1] += memo['G'][i+1][1] + memo['G'][i+1][0]
                memo['P'][i][1] += memo['P'][i+1][1] + memo['P'][i+1][0]
                memo['M'][i][1] += memo['M'][i+1][1] + memo['M'][i+1][0]

            house = garbage[i]
            for c in house:
                memo[c][i][0] += 1

        result = 0

        for c in ['G', 'P', 'M']:
            i = 0
            while True:
                result += memo[c][i][0]
                if memo[c][i][1] == 0:
                    break
                result += travel[i]
                i += 1

        return result
