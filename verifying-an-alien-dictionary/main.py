from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = [c for c in order]
        for i in range(len(words)-1):
            if not self.check(words[i], words[i+1], order):
                return False
        return True
    
    def check(self, s1: str, s2: str, order: List[str]) -> bool:
        l = min(len(s1), len(s2))

        for i in range(l):
            o1, o2 = order.index(s1[i]), order.index(s2[i])

            if o1 < o2:
                return True
            elif o1 > o2:
                return False

        if len(s1) <= len(s2):
            return True
        return False

