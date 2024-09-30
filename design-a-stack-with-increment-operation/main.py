class DoublyLinkedList:
    def __init__(self, val, nex=None, prev=None):
        self.val = val
        self.next = nex
        self.prev = prev

class CustomStack:

    def __init__(self, maxSize: int):
        self.l = maxSize
        self.c = 0
        self.root = None
        self.tail = None

    def push(self, x: int) -> None:
        if self.c == self.l:
            return

        v = DoublyLinkedList(x)
        if self.root is None:
            self.root = v
            self.tail = v
            self.c += 1

            return

        v.prev = self.tail
        self.tail.next = v
        self.tail = v
        self.c += 1

    def pop(self) -> int:
        if self.c == 0:
            return -1


        v = self.tail
        if self.c == 1:
            self.root = None
            self.tail = None
            self.c = 0

            return v.val

        self.tail = self.tail.prev
        self.tail.next = None
        self.c -= 1

        return v.val

    def increment(self, k: int, val: int) -> None:
        cur = self.root

        while cur is not None and k > 0:
            cur.val += val
            cur = cur.next
            k -= 1

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
