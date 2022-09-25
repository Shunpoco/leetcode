class Node:
    def __init__(self, v: int, n: "Node"):
        self.v = v
        self.n = n


class MyCircularQueue:

    def __init__(self, k: int):
        self.n = k
        prev = None
        for i in range(k):
            node = Node(-1, None)
            if prev is not None:
                prev.n = node
            else:
                root = node
            prev = node
            
        prev.n = root
        self.front = root
        self.rear = root
        self.p = 0
    

    def enQueue(self, value: int) -> bool:
        if self.rear.v != -1 and self.rear.n.v == -1:
            self.rear = self.rear.n
    
        if self.rear.v != -1:
            return False
        
        self.rear.v = value
        self.p += 1
        
        return True


    def deQueue(self) -> bool:
        if self.front.v == -1:
            return False

        self.front.v = -1
        if self.front == self.rear:
            self.front = self.front.n
            self.rear = self.rear.n
        else:       
            self.front = self.front.n
        self.p -= 1
        return True
        

    def Front(self) -> int:
        return self.front.v
        

    def Rear(self) -> int:
        return self.rear.v

    def isEmpty(self) -> bool:
        if self.p == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        return self.p == self.n


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
