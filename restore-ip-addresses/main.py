class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        candidates = len(s)-1
        stack = [[]]
        result = []
        while len(stack) > 0:
            v = stack.pop()
            
            if len(v) == 3:
                r, b = self.valid(s, v)
                if b:
                    result.append(r)
            
            elif len(v) == 0:
                for i in range(candidates):
                    t = v.copy()
                    t.append(i)
                    stack.append(t)
            else:
                for i in range(v[-1]+1, candidates):
                    t = v.copy()
                    t.append(i)
                    
                    if len(t) == 3 or i != candidates-1:
                        stack.append(t)
        
        return result
    
    def valid(self, s: str, nums: List[int]) -> bool:
        r = ""
        s_i = 1
        n_i = 0
        t = s[0]
        
        while n_i < 3:
            if s_i > nums[n_i]:
                if len(t) > 3 or (len(t) != 1 and t[0] == "0") or int(t) > 255:
                    return ("", False)
                r += t + "."
                n_i += 1
                t = ""
            else:
                t += s[s_i]
                s_i += 1
                
        if s_i < len(s):
            v = s[s_i:]
            r += v
            if len(v) > 3 or (len(v) != 1 and v[0] == "0") or int(v) > 255:
                return ("", False)
        
        print(r)
        return (r, True)
