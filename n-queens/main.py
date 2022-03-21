class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        stack = [[]]
        result = []
        
        while len(stack) > 0:
            candidate = stack.pop()
            
            if self.check(candidate):
                if len(candidate) == n:
                    result.append(self.convert(candidate))
                else:
                    for i in range(n):
                        t = candidate.copy()
                        t.append(i)
                        stack.append(t)
                        
        return result
    
    def check(self, candidate: List[int]) -> bool:
        if len(candidate) <= 1:
            return True
        
        for i in range(1, len(candidate)):
            # vertical
            for j in range(i):
                if candidate[i] == candidate[j]:
                    return False
                
            # diagonal, top-left
            for j in range(i):
                if candidate[i]-(i-j) == candidate[j]:
                    return False
                
            # diagonal, top-right
            for j in range(i):
                if candidate[i]+(i-j) == candidate[j]:
                    return False
                
        return True

    def convert(self, candidate: List[int]) -> List[str]:
        result = []
        for idx in candidate:
            t = ["."]*len(candidate)
            t[idx] = "Q"
            result.append("".join(t))
            
        return result
