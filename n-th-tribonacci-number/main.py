from typing import Dict

class Solution:
    def tribonacci(self, n: int) -> int:
        memory = {0: 0, 1: 1, 2: 1}

        self.exec(n, memory)

        return memory[n]


    def exec(self, n: int, memory: Dict[int, int]):
        if memory.get(n):
            return

        r = 0
        for i in range(1, 4):
            if n-i >= 0:
                self.exec(n-i, memory)
                r += memory[n-i]

        memory[n] = r
