sex = input("Input sex (f/m): ").lower()
hg = int(input("Input hemogoblin value: "))

if sex == "m":
    if hg < 134:
        print("Too low")
    elif hg > 167:
        print("Too high")
    else:
        print("Normal levels!")
elif sex == "f":
    if hg < 117:
        print("Too low")
    elif hg > 155:
        print("Too high")
    else:
        print("Normal levels!")
else:
    print("Invalid sex")
