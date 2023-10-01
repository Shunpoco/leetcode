class Solution:
    def reverseWords(self, s: str) -> str:
        c = s.split(" ")
        for i in range(len(c)):
            c[i] = self.reverse(c[i])

        return " ".join(c)

    def reverse(self, s: str) -> str:
        r = ""
        for c in s:
            r = c + r

        return r

