class Solution:
    hash_mul = 60013
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0

        max_distance_squared = 0
        current_direction = 0

        for c in commands:
            if c == -1:
                current_direction = (current_direction + 1) % 4
                continue
            
            if c == -2:
                current_direction = (current_direction + 3) % 4
                continue

            dx, dy = directions[current_direction]
            for _ in range(c):
                nx, ny = x + dx, y + dy
                if self._hash_coordinates(nx, ny) in obstacle_set:
                    break

                x, y = nx, ny

            max_distance_squared = max(max_distance_squared, x*x+y*y)

        return max_distance_squared

    def _hash_coordinates(self, x: int, y: int) -> int:
        return x + self.hash_mul * y
