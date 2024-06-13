class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        r = 0

        for a, b in zip(seats, students):
            r += abs(a-b)

        return r

