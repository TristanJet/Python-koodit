import sys

yr = int(input("Enter year: "))

remcent = yr % 100
if remcent == 0:
    remfh = yr % 400
    if remfh == 0:
        print("Leap year!")
        sys.exit()

remfour = yr % 4
if remfour == 0:
    if remcent != 0:
        print("Leap year!")
        sys.exit()

print("NOT leap year")
