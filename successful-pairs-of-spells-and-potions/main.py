
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        for spell in spells:
            t = success // spell if success % spell == 0 else success // spell + 1

            p = self.search(potions, t, 0, len(potions))

            result.append(len(potions)-p)

        return result

    def search(self, potions: List[int], target: int, start: int, end: int) -> int:
        if start == end:
            return start

        m = (start+end)//2

        # if potions[m] == target:
        #     return m

        # el
        if potions[m] < target:
            return self.search(potions, target, m+1, end)

        else:
            return self.search(potions, target, start, m)

