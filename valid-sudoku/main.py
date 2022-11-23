from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            for c in range(9):
                if not self.isValidRow(board, r) or not self.isValidColumn(board, c) or not self.isValidBlock(board, r, c):
                    return False
        return True
        
    
    def isValidRow(self, board: List[List[str]], r: int) -> bool:
        m = defaultdict(int)
        
        for i in range(9):
            if board[r][i] == ".":
                continue
            if m[board[r][i]] == 1:
                return False
            m[board[r][i]] += 1
            
        return True
    
    def isValidColumn(self, board: List[List[str]], c: int) -> bool:
        m = defaultdict(int)
        
        for i in range(9):
            if board[i][c] == ".":
                continue
            if m[board[i][c]] == 1:
                return False
            m[board[i][c]] += 1
            
        return True
    
    def isValidBlock(self, board: List[List[str]], r: int, c: int) -> bool:
        m = defaultdict(int)
        
        pr = r // 3
        pc = c // 3
        
        for i in range(3):
            for j in range(3):
                if board[i+3*pr][j+3*pc] == ".":
                    continue
                if m[board[i+3*pr][j+3*pc]] == 1:
                    return False
                m[board[i+3*pr][j+3*pc]] += 1
                
        return True
