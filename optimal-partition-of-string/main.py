from collections import defaultdict

class Solution:
    def partitionString(self, s: str) -> int:
        dic = defaultdict(int)

        result = 0
        for c in s:
            if dic[c] > 0:
                result += 1
                dic = defaultdict(int)
            dic[c] += 1

        return result + 1


