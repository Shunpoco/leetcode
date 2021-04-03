from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        c = 0

        for i in range(l):
            v = digits[l-1-i]
            if i == 0:
                nv = v + 1
            else:
                nv = v + c
            
            if nv < 10:
                digits[l-1-i] = nv
                return digits
            nv = 0
            digits[l-1-i] = nv
            c = 1

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits

