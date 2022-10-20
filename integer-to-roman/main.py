class Solution:
    def intToRoman(self, num: int) -> str:
        words = [
            ["I", "V", "X"],
            ["X", "L", "C"],
            ["C", "D", "M"],
            ["M"],
        ]
                
        result = ""
        idx = 0
        while num > 0:
            v = num % 10
            s = ""
            if v == 4:
                s += words[idx][0] + words[idx][1]
                v = 0
            elif v == 9:
                s += words[idx][0] + words[idx][2]
                v = 0
                
            while v > 0:
                if v >= 5:
                    s += words[idx][1]
                    v -= 5
                else:
                    s += words[idx][0] * v
                    v = 0

            result = s + result
                    
            
            num //= 10
            idx += 1
            
        return result
