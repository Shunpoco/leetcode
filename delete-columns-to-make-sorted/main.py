from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        n = len(strs[0])
        for i in range(n):
            t = [s[i] for s in strs]
            if not self.isSorted(t):
                result += 1

        return result

    def isSorted(self, chars: List[str]) -> bool:
        t = chars.copy()
        t.sort()

        return chars == t
