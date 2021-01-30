from typing import List

class Solution:
    def plusOne(self, digits: List[int])-> List[int]:
        
        isZero = sum(digits) == 0

        l = len(digits)

        for i in range(l):
            digits[l-1-i] += 1

            if digits[l-1-i] <= 9:
                break
            digits[l-1-i] = 0

        if digits[0] == 0 and not isZero:
            digits = [1] + digits

        return digits
