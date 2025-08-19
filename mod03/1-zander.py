maxlen = 42

zlen = int(input("Enter Zander length in centimetres: "))

if zlen < maxlen:
    print(f"Return to lake!\nZander was {maxlen - zlen} centimetres too small")
else:
    print(f"Wow! Nice catch!")
