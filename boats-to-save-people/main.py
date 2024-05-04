class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        result = 0
        left, right = 0, len(people)-1

        while left <= right:
            v1 = people[right]
            right -= 1
            if limit >= v1 + people[left]:
                left += 1
            result += 1

        return result

