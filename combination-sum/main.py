class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = [([], 0, 0)]
        result = []
        while len(stack) > 0:
            vals, res, idx = stack.pop(-1)
            
            # add candidate
            t = res + candidates[idx]
            v = vals.copy()
            v.append(candidates[idx])
            if t == target:
                result.append(v)
            elif t < target:
                stack.append((v, t, idx))

            # ignore current candidate
            if idx + 1 < len(candidates):
                stack.append((vals, res, idx+1))
                
        return result
