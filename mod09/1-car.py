class Car:
    def __init__(self, regno, max):
        self.regno = regno
        self.max = max
        self.cur = 0
        self.d = 0

def main():
    car = Car("ABC-123", 142)
    print(car.regno)
    print(car.max)
    print(car.cur)
    print(car.d)

main()
