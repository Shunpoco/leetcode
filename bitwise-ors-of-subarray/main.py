
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()

        current = {0}
        for a in arr:
            current = {a|b for b in current} | {a}
            result |= current

        return len(result)

