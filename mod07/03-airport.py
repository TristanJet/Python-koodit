import sys

opts = ('e', 'f', 'q')

ap = {
    'helsinki': 'EFHK',
    'lax': 'KLAX',
}

while 1:
    print('-------------------')
    opt = input('Fetch, Enter or quit? (e/f/q): ').lower()
    if opt not in opts:
        print('Invalid option')
        sys.exit()
    if opt == 'e':
        nam = input('Enter airport name: ').lower()
        if nam in ap.keys():
            print(f'{nam} is already in the dataset')
            continue
        icao = input('Enter ICAO: ').upper()
        ap[nam] = icao
    elif opt == 'f':
        nam = input('Enter airport name: ').lower()
        print(f'Name: {nam}\nICAO: {ap[nam]}')
    elif opt == 'q':
        break
