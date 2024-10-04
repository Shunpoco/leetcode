class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)

        total = sum(skill)

        if total % (n//2) != 0:
            return -1

        e = total // (n//2)

        skill.sort()

        result = 0
        for i in range(n // 2):
            t = skill[i] + skill[n-1-i]

            if t != e:
                return -1

            result += skill[i] * skill[n-1-i]

        return result
