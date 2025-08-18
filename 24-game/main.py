class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> True:
            if len(nums) == 1:
                return abs(nums[0]-24) < EPS

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    ops = [a+b, a-b, b-a, a*b]
                    if abs(b) > EPS:
                        ops.append(a/b)
                    if abs(a) > EPS:
                        ops.append(b/a)

                    for op in ops:
                        t = [op]
                        t.extend(next_nums)

                        if dfs(t):
                            return True

            return False

        
        return dfs([float(card) for card in cards])

