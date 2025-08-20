import sys

num = int(input("Enter positive integer:"))

if num < 0: sys.exit()

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is NOT prime")
        sys.exit()

print(f"{num} IS prime")
