class Solution:
    def removeDuplicates(self, s: str) -> str:
        idx = 0
        while idx < len(s)-1:
            if s[idx] == s[idx+1]:
                s = s[:idx]+s[idx+2:]
                idx = idx - 1 if idx > 0 else 0
                
            else:
                idx += 1
                
        return s
