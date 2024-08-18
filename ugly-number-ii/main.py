class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = set()
        uglies.add(1)

        cur = 1
        for i in range(n):
            cur = min(uglies)
            uglies.remove(cur)

            uglies.add(cur*2)
            uglies.add(cur*3)
            uglies.add(cur*5)

        return cur
