class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        calcs = [0]*len(dominoes)
        
        a = 100001
        
        s = 0
        for i in range(len(dominoes)):
            v = dominoes[i]
            
            if v == "R":
                s = a
                calcs[i] = a
            elif v == "L":
                s = 0
                calcs[i] = -a
            else:
                if s > 0:
                    s -= 1
                calcs[i] += s
                
                
        s = 0
        for i in range(len(dominoes)-1, -1, -1):
            v = dominoes[i]
            
            if v == "R":
                s = 0
                calcs[i] = a
            elif v == "L":
                s = -a
                calcs[i] = -a
            else:
                if s < 0:
                    s += 1
                calcs[i] += s
                
        r = ""
        for calc in calcs:
            if calc < 0:
                r += "L"
            elif calc > 0:
                r += "R"
            else:
                r += "."
                
        return r
