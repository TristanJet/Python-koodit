class Food:
    def __init__(self, nam, cal):
        self.nam = nam
        self.cal = cal

    def info(self):
        return self.nam, self.cal

class Fruit(Food):
    def __init__(self, nam, cal, is_sweet):
        super().__init__(nam, cal)
        self.is_sweet = is_sweet

    def pr(self):
        info = self.info()
        print(f"name: {info[0]}")
        print(f"calories: {info[1]}")
        print(f"is sweet: {self.is_sweet}")

class Vegetable(Food):
    def __init__(self, nam, cal, is_leafy):
        super().__init__(nam, cal)
        self.is_leafy = is_leafy

    def pr(self):
        info = self.info()
        print(f"name: {info[0]}")
        print(f"calories: {info[1]}")
        print(f"is leafy: {self.is_leafy}")

class Store:
    def __init__(self):
        self.inv = dict()

    def add(self, food):
        self.inv[food.nam] = food

    def show(self):
        for p in self.inv.keys():
            self.inv[p].pr()

    def buy(self, foodnam):
        if foodnam in self.inv.keys():
            return self.inv[foodnam]

class Smoothie:
    def __init__(self, n, foods):
        self.name = n
        self.foods = foods

    def info(self):
        print(self.name)
        sumcal = 0
        for f in self.foods:
            sumcal += f.cal
        print(sumcal)

def main():
    store = Store()
    store.add(Fruit("apple", 30, True))
    store.add(Vegetable("broccoli", 25, True))
    store.show();
    inp = ""
    ls = []
    while 1:
        inp = input("What do you want to buy, empty to exit: ")
        if inp == "":
            break
        else:
            bought = store.buy(inp)
            if bought != None:
                ls.append(bought)
    smoothie = Smoothie("COOL-SMOOTHIE", ls)
    smoothie.info()

main()
