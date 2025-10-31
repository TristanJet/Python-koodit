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
