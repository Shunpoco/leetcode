class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = {}
        for c in t:
            if mem.get(c) is None:
                mem[c] = 1
            else:
                mem[c] += 1
            
        l, r = 0, 0
        c = len(t)
        result = ""
        while r < len(s):
            while c > 0:
                if r == len(s):
                    return result
                v = s[r]
                if mem.get(v) is not None:
                    if mem[v] > 0:
                        c -= 1
                    mem[v] -= 1
                r += 1
            st = s[l:r]
            if result == "" or len(result) > len(st):
                result = st
            while l <= r:
                v = s[l]
                if mem.get(v) is None:
                    l += 1
                    st = s[l:r]
                    if result == "" or len(result) > len(st):
                        result = st
                elif mem[v] < 0:
                    l += 1
                    mem[v] += 1
                    st = s[l:r]
                    if result == "" or len(result) > len(st):
                        result = st
                else:
                    mem[v] += 1
                    c += 1
                    l += 1
                    break
                        
        return result
