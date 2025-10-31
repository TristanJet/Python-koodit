class Publication:
    def __init__(self, name) -> None:
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pgc) -> None:
        self.name = name
        super().__init__(name)
        self.author = author
        self.page_count = pgc

    def printinfo(self) -> None:
        print("------------------------------")
        print(f"{self.name}\nAuthor: {self.author}\nPage count: {self.page_count}")

class Mag(Publication):
    def __init__(self, name, chiefe) -> None:
        self.name = name
        super().__init__(name)
        self.chiefe = chiefe

    def printinfo(self) -> None:
        print("------------------------------")
        print(f"{self.name}\nChief editor: {self.chiefe}")

def main():
    publications = []
    publications.append(Mag("Aku Ankka", "Aki Hyyppa"))
    publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))
    for pub in publications:
        pub.printinfo()

main()
