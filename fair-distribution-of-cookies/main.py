from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        r = [0 for _ in range(k)]

        return self.bt(0, 0, cookies, r)

    def bt(self, idx: int, zero: int, cookies: List[int], r: List[int]) -> int:
        if idx == len(cookies):
            return max(r)

        result = -1
        for i in range(zero+1):
            v = zero
            if zero < len(r)-1 and r[i] == 0:
                v += 1
            r[i] += cookies[idx]
            t = self.bt(idx+1, v, cookies, r)
            if result == -1 or result > t:
                result = t
            r[i] -= cookies[idx]

        return result

