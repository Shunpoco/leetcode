
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            if i == 0:
                result.append([1])
                continue
            elif i == 1:
                result.append([1, 1])
                continue

            t = [0] * (i+1)
            t[0], t[-1] = 1, 1
            for j in range(i-1):
                t[j+1] = result[i-1][j] + result[i-1][j+1]

            result.append(t)

        return result


