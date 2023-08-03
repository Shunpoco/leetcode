class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        stack = [""]
        result = []
        while len(stack) > 0:
            v = stack.pop(-1)

            if len(v) == n:
                result.append(v)
                continue

            c = digits[len(v)]

            for a in map.get(c):
                stack.append(v+a)

        return result
