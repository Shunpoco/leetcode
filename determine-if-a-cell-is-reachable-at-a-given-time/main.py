class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(sx - fx)
        dy = abs(sy - fy)

        mint = max(dx, dy)

        if t < mint:
            return False
        
        if dx == 0 and dy == 0 and t == 1:
            return False

        return True
