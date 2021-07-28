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


# 2021-07-28
import queue

class Solution:
    def isValid(self, s: str) -> bool:
        combs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        
        stack = queue.LifoQueue() # LIFOQueue = Stack
        
        for c in s:
            if c in combs.keys():
                if stack.empty():
                    return False
                v = stack.get()
                if combs[c] != v:
                    return False
                
            else:
                stack.put(c)
                
                
        if not stack.empty():
            return False
        
        return True
