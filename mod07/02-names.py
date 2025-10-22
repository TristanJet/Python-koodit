names = set()

while 1:
    nam = input("Enter name: ").lower()
    if len(nam) == 0:
        break
    if nam in names:
        print('Existing name')
    else:
        print('New name')
    names.add(nam)
print('\nAll names: ')
for n in names:
    print(n)
