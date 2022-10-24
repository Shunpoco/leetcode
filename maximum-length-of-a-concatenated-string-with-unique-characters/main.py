from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        bits = []
        
        for s in arr:
            v = 0
            dup = False
            for c in s:
                converted = 1<<(ord(c) - ord('a'))
                if v ^ converted != v | converted:
                    dup = True
                    break
                v += converted
                
            if dup == False:
                c = str(bin(v))
                t = 0
                for c_ in c:
                    if c_ == "1":
                        t += 1
                
                bits.append((v, t))
                
        def bt(idx: int, cur: int, cur_num: int) -> int:
            result = cur_num
            if idx == len(bits):
                return result
            
            for i in range(idx+1, len(bits)):
                v, t = bits[i]
                if v ^ cur != v | cur:
                    continue
                
                r = bt(i, cur|v, cur_num+t)
                
                if result < r:
                    result = r
            
            return result
                
        result = bt(-1, 0, 0)
        
        return result
