class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        stack = [([], 0, target)]
        result = []

        while len(stack) > 0:
            cur, level, ct = stack.pop(-1)

            for i in range(level, len(candidates)):
                num = candidates[i]
                if i == level or num != candidates[i-1]:
                    if ct - num == 0:
                        t = cur.copy()
                        t.append(num)
                        result.append(t)

                    elif ct - num > 0:
                        t = cur.copy()
                        t.append(num)
                        stack.append((t, i+1, ct-num))

        return result
