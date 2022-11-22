class Solution:
    memory = {0: 0, 1: 1}
    
    
    def numSquares(self, n: int) -> int:
        if self.memory.get(n) is not None:
            return self.memory[n]
        
        t = 1
        while t*t <= n:
            t += 1
            
        t -= 1
        result = 1000000
        while t > 0:
            tn = n - t*t
            tv = self.numSquares(tn) + 1
            
            if result > tv:
                result = tv
            
            t -= 1
            
        self.memory[n] = result
        
        return result
