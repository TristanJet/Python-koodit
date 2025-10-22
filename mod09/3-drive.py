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
    car = Car("ABC-123", 142)
    car.accel(30)
    car.accel(70)
    car.accel(50)
    print(car.speed)
    car.drive(2)
    print(car.d)
    car.accel(-50)
    car.drive(1)
    print(car.d)

main()
