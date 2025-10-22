import random

class Car:
    def __init__(self, regno, max):
        self.regno = regno
        self.max = max
        self.speed = 0
        self.d = 0
    
    def accel(self, delta):
        self.speed += delta
        if self.speed > self.max:
            self.speed = self.max
        if self.speed < 0:
            self.speed = 0

    def drive(self, hr):
        self.d += self.speed * hr

def main():
    cars = list()
    for i in range(1, 11):
        cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

    race = True
    while race:
        for i in range(len(cars)):
            car = cars[i]
            car.accel(random.randint(-10, 15))
            car.drive(1)
            if car.d >= 10000:
                race = False

    cars.sort(key=lambda c: c.d, reverse=True)
    for i in range(len(cars)): 
        c = cars[i]
        print(f"{i+1}. Reg: {c.regno} | Distance: {c.d} | Speed: {c.speed} | Max speed: {c.max}")

main()
