import random

class RandomizedSet:

    def __init__(self):
        self.storage = {}

    def insert(self, val: int) -> bool:
        if self.storage.get(val) is not None:
            return False
        self.storage[val] = True
        return True

    def remove(self, val: int) -> bool:
        try:
            return self.storage.pop(val)

        except:
            return False

    def getRandom(self) -> int:
        v = random.randint(0, len(self.storage)-1)
        return list(self.storage.keys())[v]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
