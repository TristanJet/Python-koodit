def main():
    val1 = getInput()
    priceArea(val1)
    val2 = getInput()
    priceArea(val2)
    if val1 < val2:
        print(f"The first pizza is cheaper value")
    else:
        print(f"The second pizza is cheaper value")

def getInput():
    d = int(input("Enter diameter (cm): "))
    p = int(input("Enter price (e): "))
    return (d, p)

def priceArea(x):
    r = x[0] / 2
    a = 3.14 * (r * r)
    return x[1] / a

main()
