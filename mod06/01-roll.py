import random

def main():
    val = 0
    while val != 6:
        val = roll()
        print(f"Dice value: {val}")

def roll():
    return random.randint(1, 6)

main()
