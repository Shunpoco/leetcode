from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memory = {}
        
        def isPalindrome(s: str) -> bool:
            m = int(len(s)/2)
            for i in range(m):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        
        def part(s: str) -> List[List[str]]:
            if memory.get(s):
                return memory[s]

            l = len(s)
            result = []
            for i in range(l):
                left = s[:i+1]
                if isPalindrome(left):
                    if len(left) == l:
                        result.append([left])
                        break
                    res = [left]
                    right = s[i+1:]
                    v = part(right)
                    for r in v:
                        temp = res.copy()
                        temp.extend(r)
                        result.append(temp)
            memory[s] = result
            return result

        return part(s)
