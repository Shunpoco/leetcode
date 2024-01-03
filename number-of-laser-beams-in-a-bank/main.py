class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) == 1:
            return 0
        
        counter = [0 for _ in range(len(bank))]

        for i, b in enumerate(bank):
            for c in b:
                if c == '1':
                    counter[i] += 1

        
        idx = 0
        result = 0
        while idx < len(bank)-1:
            right = idx + 1

            while right < len(bank) and counter[right] == 0:
                right += 1

            if right == len(bank):
                break

            result += counter[idx] * counter[right]

            idx = right

        return result
