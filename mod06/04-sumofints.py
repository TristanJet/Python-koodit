def main():
    x = [1, 2, 3, 4, 5, 6]
    print(f"List: {x}\nSum: {sum(x)}")

def sum(ls):
    sum = 0
    for x in ls:
        sum += x
    return sum

main()
