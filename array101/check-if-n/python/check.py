from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h1 = {}
        h2 = {}
        for num in arr:
            if h1.get(num*2) is None and h2.get(num) is None:
                h1[num] = 1
                h2[num*2] = 1
            else:
                return True

        return False
