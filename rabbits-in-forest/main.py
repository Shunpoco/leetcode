class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        memo = defaultdict(int)

        for answer in answers:
            memo[answer] += 1

        result = 0

        for k, v in memo.items():
            if k == 0:
                result += v
            elif v <= (k+1):
                result += k + 1
            else:
                result += ceil(float(v)/(k+1)) * (k+1)

        return result

