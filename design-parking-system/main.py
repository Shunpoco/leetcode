from collections import Counter

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parks = Counter()
        self.limits = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parks[carType] >= self.limits[carType]:
            return False
        self.parks[carType] += 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
