def main():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"List: {x}\nEven: {remOdd(x)}")

def remOdd(ls):
    even = []
    for x in ls:
        if x % 2 == 0:
            even.append(x)
    return even

main()
