factor = 4.54609

def main():
    while 1:
        gallons = int(input("Enter N gallons: "))
        if gallons < 0:
            return
        print(f"{gallons} gallons is equivalent to {round(gtl(gallons), 3)} litres")

def gtl(g):
    return g * factor

main()
