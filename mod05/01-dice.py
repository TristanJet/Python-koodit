import random

d = int(input("How many dice?: "))
sum = 0

for i in range(0, d):
    sum += random.randrange(1, 7)

print(f"sum of {d} dice is {sum}")
