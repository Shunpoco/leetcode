class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            dominoes[i].sort()

        dominoes.sort()

        result = 0

        idx = 0

        while idx < len(dominoes):
            v = dominoes[idx]
            c = 1
            t = idx + 1
            while t < len(dominoes) and v[0] == dominoes[t][0] and v[1] == dominoes[t][1]:
                c += 1
                t += 1

            if c > 1:
                result += c * (c - 1) // 2
            idx = t

        return result

