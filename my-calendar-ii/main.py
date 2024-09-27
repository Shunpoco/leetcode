class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for b in self.overlaps:
            if self.is_overlap(b[0], b[1], start, end):
                return False

        for b in self.bookings:
            if self.is_overlap(b[0], b[1], start, end):
                self.overlaps.append(
                    self.get_overlap(b[0], b[1], start, end)
                )

        self.bookings.append((start, end))

        return True

    def is_overlap(self, start1, end1, start2, end2):
        return max(start1, start2) < min(end1, end2)

    def get_overlap(self, start1, end1, start2, end2):
        return max(start1, start2), min(end1, end2)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
