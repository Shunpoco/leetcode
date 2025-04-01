class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = [-1 for _ in range(len(questions))]

        self.calc(0, questions, memo)

        return memo[0]

    
    def calc(self, idx, questions, memo):
        if memo[idx] > -1:
            return

        # Take this question
        v = questions[idx]
        result = v[0]
        next_idx = idx + v[1] + 1
        if next_idx < len(questions):
            self.calc(next_idx, questions, memo)
            result += memo[next_idx]

        # Skip the question
        next_idx = idx + 1
        if next_idx < len(questions):
            self.calc(next_idx, questions, memo)
            t = memo[next_idx]

            if t > result:
                result = t

        memo[idx] = result

