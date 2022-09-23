class Solution:
    def concatenatedBinary(self, n: int) -> int:
        r = 1
        i = 1
        b = 2
        
        for v in range(2, n+1):
            if b <= v:
                b *= 2
                i += 1
            r = (r << i) + v
            r %= 1000000007
            
        return r
