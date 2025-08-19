import random

seq1 = [0, 0, 0]
seq2 = [0, 0, 0, 0]

i = 0
while i < 3 :
    seq1[i] = random.randrange(0, 10)
    i+=1

print(f"Code 1: {seq1}")

i = 0
while i < 4 :
    seq2[i] = random.randrange(1, 7)
    i+=1

print(f"Code 2: {seq2}")
