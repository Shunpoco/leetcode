class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiral(matrix, [])
    
    def spiral(self, matrix: List[List[int]], result: List[int]) -> List[int]:
        col = len(matrix[0])
        row = len(matrix)
        count = 0
        for i in range(col):
            result.append(matrix[0][i])
            count += 1
        for i in range(1, row):
            result.append(matrix[i][col-1])
            count += 1
        if row > 1:
            for i in range(col-2, -1, -1):
                result.append(matrix[row-1][i])
                count += 1
        
        if row > 2 and col > 1:
            for i in range(row-2, 0, -1):
                result.append(matrix[i][0])
                count += 1
                
        if count < col * row:
            next_matrix = []
            for i in range(1, row-1):
                next_matrix.append(matrix[i][1:col-1])
            return self.spiral(next_matrix, result)
            
        return result
        
