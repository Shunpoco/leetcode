class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        for i in range(1, 10):
            self.calc(i, n, result)

        return result


    def calc(self, cur, limit, result):
        if cur > limit:
            return

        result.append(cur)

        for i in range(10):
            t = cur * 10 + i

            if t <= limit:
                self.calc(t, limit, result)

            else:
                break

