import random

num = random.randrange(1, 11)

print("I am thinking of a number between 1 and 10")

i = 1
while 1:
    inp = int(input("Enter guess: "))
    if inp == num:
        print(f"Correct! You took {i} tries.")
        break
    elif inp < num:
        print("Too low")
    else:
        print("Too high")
    i+=1
