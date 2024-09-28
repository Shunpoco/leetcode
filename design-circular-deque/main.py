class LinkedList:
    def __init__(self, value: int, n=None):
        self.value = value
        self.next = n

class MyCircularDeque:

    def __init__(self, k: int):
        self.max = k
        self.l = 0
        self.root = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        nr = LinkedList(value, self.root)
        self.root = nr
        self.l += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.root is None:
            self.root = LinkedList(value)
            self.l = 1

            return True

        cur = self.root
        while cur.next is not None:
            cur = cur.next

        cur.next = LinkedList(value)
        self.l += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.root = self.root.next
        self.l -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        cur = self.root
        if cur.next is None:
            self.root = None
            self.l = 0

            return True

        while cur.next.next is not None:
            cur = cur.next

        cur.next = None
        self.l -= 1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.root.value        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        cur = self.root
        while cur.next is not None:
            cur = cur.next

        return cur.value

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.max


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
