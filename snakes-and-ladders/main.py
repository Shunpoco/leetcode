from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        labels = {}
        ascend = True
        t = 1
        for r in range(n-1, -1, -1):
            if ascend:
                for c in range(n):
                    labels[t] = (r, c)
                    t += 1
            else:
                for c in range(n-1, -1, -1):
                    labels[t] = (r, c)
                    t += 1
            ascend ^= True

        default = 9999999
        paths = [[default for _ in range(n)] for _ in range(n)]
        paths[n-1][0] = 0
        queue = [(1, n-1, 0, 0)]
        while len(queue) > 0:
            cur, crow, ccol, cpath = queue.pop(0)
            for nex in range(cur+1, min(cur+6, n*n)+1):
                row, col = labels[nex]
                if board[row][col] != -1:
                    nex = board[row][col]
                    row, col = labels[nex]
                if paths[row][col] > cpath+1:
                    paths[row][col] = cpath+1
                    if nex != n*n:
                        queue.append((nex, row, col, cpath+1))
        
        if n%2 == 0:
            if paths[0][0] == default:
                return -1
            return paths[0][0]
        else:
            if paths[0][n-1] == default:
                return -1
            return paths[0][n-1]
