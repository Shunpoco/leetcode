from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        memory = defaultdict(int)
        for task in tasks:
            memory[task] += 1

        result = 0
        for _, val in memory.items():
            v = self.executable(val)
            if v == -1:
                return -1
            result += v

        return result

    def executable(self, val: int) -> int:
        if val == 0:
            return 0
        elif val <= 1:
            return -1

        for i in [3, 2]: # Because If it is suitable, consuming three tasks is better than consuming two tasks.
            t = self.executable(val-i)
            if t != -1:
                return t+1

        return -1
