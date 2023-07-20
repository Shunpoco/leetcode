from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop(-1)
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == -a:
                    stack.pop(-1)
            else:
                stack.append(a)

        return stack

