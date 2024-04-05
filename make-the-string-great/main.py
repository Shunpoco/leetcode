class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s)-1:
            if (s[i].upper() == s[i+1] or s[i+1].upper() == s[i]) and s[i] != s[i+1]:
                s = s[:i] + s[i+2:]
                i = i - 1 if i > 0 else 0 
            else:
                i += 1
            
        return s


