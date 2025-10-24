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

def main():
    e = Elevator(1, 6)
    e.goTo(4)
    print(e.floor)
    e.goTo(1)
    print(e.floor)

main()
