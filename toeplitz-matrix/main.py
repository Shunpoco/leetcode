from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        
        m = [-1 for _ in range(c)]
        
        for i in range(r):
            t = [-1 for _ in range(c)]
            for j in range(c):
                if m[j] != -1 and m[j] != matrix[i][j]:
                    return False
                if j < c-1:
                    t[j+1] = matrix[i][j]
                    
            m = t
                    
        return True
