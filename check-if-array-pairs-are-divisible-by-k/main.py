class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        memo = defaultdict(list)

        for num in arr:
            memo[num % k].append(num)

        print(memo)
        for key, value in memo.items():
            if key == 0 and len(value) % 2 != 0:
                return False

            elif key != 0:
                diff = k - key
                if memo.get(diff) is None or len(memo[diff]) != len(value):
                    return False

        return True
