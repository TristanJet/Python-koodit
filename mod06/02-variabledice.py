import random

nsides = 99

def main():
    val = 0
    while val != nsides:
        val = roll(nsides)
        print(f"Dice value: {val}")

def roll(n):
    return random.randint(1, n)

main()
