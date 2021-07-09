class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        d = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        
        stack = []
        
        stack.append(s[0])

        for i in range(1, len(s)):
            c = s[i]
            if c not in d:
                stack.append(c)
                continue

            if not stack:
                return False
            
            if d[c] == stack[-1]:
                stack.pop(-1)
                
            else:
                return False
    
        if stack:
            return False
        
        return True
