from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))

        memo = [-1 for _ in range(len(words))]

        for i in range(len(words)-1, -1, -1):
            self.calc(i, words, memo)
        
        return max(memo)

    def calc(self, idx: int, words: List[str], memo: List[int]):
        if memo[idx] >= 0:
            return

        if idx == len(words)-1:
            memo[idx] = 1
            return

        r = 1

        nex = idx+1

        while nex < len(words) and len(words[nex]) <= len(words[idx])+1:
            if len(words[nex]) == len(words[idx]) + 1 and self.check(words[idx], words[nex]):
                self.calc(nex, words, memo)
                t = 1 + memo[nex]
                if t > r:
                    r = t

            nex += 1

        memo[idx] = r

        return

    def check(self, w1: str, w2: str) -> bool:
        i1, i2 = 0, 0
        c = 0

        while i2 < len(w2):
            if i1 < len(w1) and w1[i1] != w2[i2]:
                if c == 0:
                    c += 1
                    i2 += 1
                else:
                    return False

            else:
                i1 += 1
                i2 += 1

        return True

