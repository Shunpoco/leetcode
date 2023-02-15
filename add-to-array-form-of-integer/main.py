from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num2 = []
        while k > 0:
            num2.insert(0, k%10)
            k = k // 10

        r = []
        c = 0
        l = max(len(num), len(num2))
        for i in range(l):
            a = num[len(num)-i-1] if len(num)-i-1 >= 0 else 0
            b = num2[len(num2)-i-1] if len(num2)-i-1 >= 0 else 0

            v = a + b + c
            if v > 9:
                c = 1
                v -= 10
            else:
                c = 0
            r.insert(0, v)

        if c > 0:
            r.insert(0, 1)

        return r

