class Solution:
    def maxDifference(self, s: str) -> int:
        counter = [0] * 26

        for c in s:
            counter[ord(c)-ord('a')] += 1

        max_odd = 0
        min_even = float('inf')

        for count in counter:
            if count == 0:
                continue
            if count % 2 == 0 and count < min_even:
                min_even = count
            elif count % 2 != 0 and count > max_odd:
                max_odd = count

        return max_odd - min_even
