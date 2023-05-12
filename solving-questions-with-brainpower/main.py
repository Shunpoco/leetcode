from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = [-1 for _ in range(len(questions))]

        self.exec(0, questions, memo)

        return memo[0]

    
    def exec(self, idx: int, questions: List[List[int]], memo: List[int]):
        if memo[idx] >= 0:
            return

        if idx == len(questions)-1:
            memo[idx] = questions[idx][0]
            return

        if idx+questions[idx][1]+1 < len(questions):
            self.exec(idx+questions[idx][1]+1, questions, memo)
        
        self.exec(idx+1, questions, memo)

        memo[idx] = max(
            questions[idx][0]+memo[idx+questions[idx][1]+1],
            memo[idx+1],
        ) if idx+questions[idx][1]+1 < len(questions) else max(
            questions[idx][0],
            memo[idx+1],
        )
        return

