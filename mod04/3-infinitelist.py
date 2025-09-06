ls = []
while 1:
    try:
        x = int(input("Enter a number to add, string to exit: "))
        ls.append(x)
    except ValueError:
        if len(ls) > 1:
            ls.sort()
            print(f"Smallest inputted: {ls[0]}\nLargest inputted: {ls[-1]}")
        else:
            print(f"Only item: {ls[0]}")
        break
