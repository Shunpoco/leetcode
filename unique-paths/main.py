class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = {}
        
        return self.paths(m, n, memory)                
    
    def paths(self, m: int, n: int, mem: Dict) -> int:
        if mem.get((m, n)) is not None:
            return mem.get((m, n))
            
        if m == 1 or n == 1:
            v = 1

        else:
            v1 = self.paths(m-1, n, mem)
            v2 = self.paths(m, n-1, mem)
            v = v1 + v2

        mem[(m, n)] = v
        
        return v
