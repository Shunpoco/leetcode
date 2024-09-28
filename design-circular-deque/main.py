class MyCircularDeque:

    def __init__(self, k: int):
        self.max = k
        self.q = []

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q.insert(0, value)

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q.append(value)

        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.q.pop(0)

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.q.pop(-1)

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.max


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
