import sys

yr = int(input("Enter year: "))

remfour = yr % 4
remcent = yr % 100

if remcent == 0:
    remfh = yr % 400
    if remfh == 0:
        print("Leap year!")
        sys.exit()

if remfour == 0:
    if remcent != 0:
        print("Leap year!")
        sys.exit()

print("NOT leap year")
