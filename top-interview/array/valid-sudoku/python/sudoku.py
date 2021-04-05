from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for digits in board:
            if self._valid(digits) == False:
                return False
            
        # column
        for i in range(0,9): # columns
            digits = []
            for j in range(0,9): # rows
                digits.append(board[j][i])

            if self._valid(digits) == False:
                return False

        # sub-box
        for k in range(0,3):
            for l in range(0, 3):
                digits = []
                for i in range(0,3):
                    for j in range(0,3):
                        digits.append(board[3*k+i][3*l+j])
                if self._valid(digits) == False:
                    return False

        return True

    def _valid(self, digits: List[str]) -> bool:
        h = {
            '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '.': 0,
        }

        for d in digits:
            if h.get(d) is None:
                return False
            if d != '.' and h.get(d) > 0:
                return False
            h[d] += 1

        return True