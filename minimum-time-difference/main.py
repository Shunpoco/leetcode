class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        tps = []
        for tp in timePoints:
            tps.append(self.convert(tp))

        tps.sort()

        result = float('inf')

        for i in range(len(tps)):
            if i == len(tps)-1:
                t = tps[0] + (60 * 24) - tps[i]

            else:
                t = tps[i+1] - tps[i]

            if t < result:
                result = t

        return result


    def convert(self, tp: str) -> int:
        v = tp.split(":")

        return int(v[0]) * 60 + int(v[1])
