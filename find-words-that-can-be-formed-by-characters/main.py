from typing import List
from collections import defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for word in words:
            memo = defaultdict(int)
            for c in chars:
                memo[c] += 1

            i = 0
            for c in word:
                if memo.get(c) is not None and memo[c] > 0:
                    memo[c] -= 1
                    i += 1
                else:
                    break

            if i == len(word):
                result += len(word)

        return result
