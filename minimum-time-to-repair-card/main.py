class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, cars * cars * ranks[0]

        while low < high:
            m = (low + high) // 2
            repaired = sum(int((m / rank) ** 0.5) for rank in ranks)

            if repaired < cars:
                low = m + 1
            else:
                high = m

        return low

