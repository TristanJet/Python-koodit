opts = ('e', 'f', 'q')

ap = {
    'helsinki': 'EFHK',
    'lax': 'KLAX',
}

while 1:
    print('-------------------')
    opt = input('Fetch, Enter or quit? (f/e/q): ').lower()
    if opt not in opts:
        print('Invalid option')
        continue
    if opt == 'e':
        nam = input('Enter airport name: ').lower()
        if nam in ap.keys():
            print(f'{nam} is already in the dataset')
            continue
        ap[nam] = input('Enter ICAO: ').upper() 
    elif opt == 'f':
        nam = input('Enter airport name: ').lower()
        if nam not in ap.keys():
            print(f'{nam} is NOT in dataset\nUnable to find')
            continue
        print(f'Name: {nam}\nICAO: {ap[nam]}')
    elif opt == 'q':
        break
