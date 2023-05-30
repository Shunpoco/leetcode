class MyHashSet:

    def __init__(self):
        self.memory = [0 for _ in range(1000001)]
        

    def add(self, key: int) -> None:
        self.memory[key] = 1

    def remove(self, key: int) -> None:
        self.memory[key] = 0

    def contains(self, key: int) -> bool:
        if self.memory[key] == 1:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
