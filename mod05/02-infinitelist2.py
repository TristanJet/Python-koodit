ls = []
while 1:
    try:
        raw = int(input("Enter a number to add, string to exit: "))
        x = int(raw)
        ls.append(x)
    except ValueError:
        if len(ls) > 2:
            ls.sort(reverse=True)
            top = ls[0:5]
            print(f"Greatest numbers inputted:")
            for i in top:
                print(i)
        else:
            print(f"Only item: {ls[0]}")
        break
