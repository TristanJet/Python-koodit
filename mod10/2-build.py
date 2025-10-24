class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = 0

    def goTo(self, f):
        if f < self.bottom or f > self.top:
            raise OverflowError
        if f < self.floor:
            self.floorDown(self.floor - f)
        elif f > self.floor:
            self.floorUp(f - self.floor)

    def floorUp(self, d):
        i = 0
        while i < d:
            self.floor += 1
            i+=1

    def floorDown(self, d):
        i = 0
        while i < d:
            self.floor -= 1
            i+=1

class Building:
    def __init__(self, bottom, top, nel):
        self.bottom = bottom
        self.top = top
        self.nel = nel
        els = []
        for x in range(nel):
            els.append(Elevator(bottom, top))
        self.els = els 

    def runElevator(self, i, dfl):
        if i >= len(self.els):
            raise IndexError
        self.els[i].goTo(dfl)

def main():
    b = Building(1, 10, 4)
    b.runElevator(3, 6)
    b.runElevator(0, 3)
    print(b.els[3].floor)
    print(b.els[0].floor)

main()
