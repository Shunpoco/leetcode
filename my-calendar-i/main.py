class MyCalendar:

    def __init__(self):
        self.memo = []

    def book(self, start: int, end: int) -> bool:
        for v in self.memo:
            if v[0] < end and start < v[1]:
                return False

        self.memo.append((start, end))
        self.memo.sort()
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
