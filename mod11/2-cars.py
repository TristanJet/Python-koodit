import random
from car import Car

class ElectricCar(Car):
    def __init__(self, regno, max, batcap):
        super().__init__(regno, max)
        self.batcap = batcap
        
class GasCar(Car):
    def __init__(self, regno, max, tankvol):
        super().__init__(regno, max)
        self.tankvol = tankvol

def main():
    ec = ElectricCar("ABC-15", 180, 52.5)
    gc = GasCar("ABC-123", 165, 32.3)
    for i in range(3):
        ec.accel(random.randint(-10, 15))
        gc.accel(random.randint(-10, 15))
        ec.drive(1)
        gc.drive(1)
    print(f"Electric car distance: {ec.d}")
    print(f"Gasoline car distance: {gc.d}")

main()
