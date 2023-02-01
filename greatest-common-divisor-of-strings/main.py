class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        if l1 < l2:
            l1, l2 = l2, l1
            str1, str2 = str2, str1

        for i in range(l1, 1, -1):
            v = str2[0:i]
            if self.check(v, str1) and self.check(v, str2):
                return v

        return ""

    def check(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l2 % l1 != 0:
            return False

        for i in range(l2//l1):
            v = s2[l1*i:l1*i+l1]
            if v != s1:
                return False

        return True

