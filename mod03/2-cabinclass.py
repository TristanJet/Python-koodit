cl = input("Enter cabin class: ").upper()

if cl == "LUX":
    print("upper-deck cabin with a balcony")
elif cl == "A":
    print("above the car deck, equipped with a window.")
elif cl == "B":
    print("windowless cabin above the car deck")
elif cl == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
