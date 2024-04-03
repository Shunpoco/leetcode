class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        for r in range(m):
            for c in range(n):
                if self.execute(r, c, 0, word, board):
                    return True
                
        return False
    
    def execute(self, r: int, c: int, pos: int, word: str, board: List[List[str]]) -> bool:
        if pos == len(word):
            return True
        
        if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
            return False
        
        if board[r][c] != word[pos]:
            return False
        
        v = board[r][c]
        board[r][c] = "!"
        
        if self.execute(r-1, c, pos+1, word, board) or self.execute(r+1, c, pos+1, word, board) or self.execute(r, c-1, pos+1, word, board) or self.execute(r, c+1, pos+1, word, board):
            return True
        
        board[r][c] = v
        return False
