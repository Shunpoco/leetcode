def isBadVersion(version):
    return True

class Solution:
    def firstBadVersion(self, n) -> int:
        return self._bad(1, n)


    def _bad(self, first: int, last: int) -> int:
        if first == last:
            return first

        m = int((first + last -1) / 2)

        if isBadVersion(m):
            return self._bad(first, m)

        return self._bad(m+1, last)