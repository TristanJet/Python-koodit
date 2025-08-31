import random

n = int(input("Enter how many points to generate: "))
# n = 1000

pcircle = 0
i = 0
while i < n:
    px = random.uniform(-1, 1)
    py = random.uniform(-1, 1)
    if px**2 + py**2 < 1:
        pcircle += 1
    i+=1

pi = (4 * pcircle) / n
print(f"Out of {n} random points in the square, {pcircle} were in the circle")
print(f"Pi estimate: {pi}")
