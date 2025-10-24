import random
from car import Car

class Race:
    def __init__(self, name, d, cars):
        self.name = name
        self.d = d
        self.cars = cars

    def passHour(self):
        for i in range(len(self.cars)):
            car = self.cars[i]
            car.accel(random.randint(-10, 15))
            car.drive(1)

    def getStatus(self) -> str:
        self.cars.sort(key=lambda c: c.d, reverse=True)
        table = ""
        bar = "-"
        i = 1
        for c in self.cars:
            table += f"| {i}. {c.regno} | travelled: {c.d} km | current speed: {c.speed} km/h | max speed: {c.max} km/h |\n"
            if i == 1:
                bar *= len(table) - 1
                bar += "\n"
            i +=1
        return bar + table + bar

    def isFinished(self) -> bool:
        for c in self.cars:
            if c.d >= self.d:
                return True
        return False


def main():
    name ="Grand Demolition Derby" 
    dist = 8000
    cars = list()
    for i in range(1, 11):
        cars.append(Car(f"ABC-{i}", random.randint(100, 200)))
    race = Race(name, dist, cars)

    hr = 0
    fin = False
    while fin == False:
        race.passHour()
        if hr % 10 == 0: print(race.getStatus())
        fin = race.isFinished()
        hr += 1
    print("RACE FINISHED")
    print(race.getStatus())

main()
