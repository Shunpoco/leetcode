class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if self.hasZero(i) and self.hasZero(n-i):
                return [i, n-i]

        return [0, 0]


    def hasZero(self, n):
        if n == 0:
            return False

        while n > 0:
            if n % 10 == 0:
                return False
            
            n //= 10

        return True
