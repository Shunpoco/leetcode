from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = len(A)
        i = 0
        c = 0
        while c < l:
            v = A[i]
            if v % 2 == 0:
                i += 1
            else:
                A[i:l-1] = A[i+1:]
                A[l-1] = v
            c += 1

        return A
 