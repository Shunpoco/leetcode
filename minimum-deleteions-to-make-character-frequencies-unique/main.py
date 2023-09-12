class Solution:
    def minDeletions(self, s: str) -> int:
        counter = [0 for _ in range(26)]

        for c in s:
            counter[ord(c)-97] += 1

        counter.sort()


        r = 0
        for i in range(25, 0, -1):
            for j in range(i-1, -1, -1):
                if counter[i] == counter[j] and counter[i] != 0:
                    counter[j] -= 1
                    r += 1

        return r

