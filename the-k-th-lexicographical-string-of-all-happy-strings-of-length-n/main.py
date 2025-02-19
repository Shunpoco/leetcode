class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        cur = ""
        result = []

        self.calc(n, cur, result)

        if len(result) < k:
            return ""

        result.sort()

        return result[k-1]

    def calc(self, n, cur, result):
        if len(cur) == n:
            result.append(cur)
            return

        for c in ["a", "b", "c"]:
            if len(cur) > 0 and cur[-1] == c:
                continue
            self.calc(n, cur+c, result)

