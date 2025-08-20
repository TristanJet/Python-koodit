ls = []
while 1:
    try:
        raw = int(input("Enter a number to add, string to exit: "))
        x = int(raw)
        ls.append(x)
    except ValueError:
        if len(ls) > 2:
            ls.sort()
            print(f"Smallest inputted: {ls[0]}\nLargest inputted: {ls[-1]}")
        else:
            print(f"Only item: {ls[0]}")
        break
