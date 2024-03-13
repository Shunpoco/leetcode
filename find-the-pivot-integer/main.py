class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = n * (n+1) // 2

        t = 0
        for i in range(1, n+1):
            t += i

            if (sum+i)%2 == 0 and (sum+i)//2 == t:
                return i

        return -1
