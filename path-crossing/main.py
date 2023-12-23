class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0): True}

        x, y = 0, 0

        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            else:
                x -= 1

            if visited.get((x, y)) is not None:
                return True

            visited[(x, y)] = True

        return False
