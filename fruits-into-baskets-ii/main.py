class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = len(fruits)

        for fruit in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    result -= 1
                    baskets[i] = -1
                    break
        return result

