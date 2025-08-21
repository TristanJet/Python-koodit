import sys

seasons = ('winter', 'spring', 'summer', 'autumn')

map = {
    'january': 0,
    'february': 0,
    'march': 1,
    'april': 1,
    'may': 1,
    'june': 2,
    'july': 2,
    'august': 2,
    'september': 3,
    'october': 3,
    'november': 3,
    'december': 0,
}

mo = input('Enter month: ').lower()

if mo not in map.keys():
    print('Invalid month')
    sys.exit()

print(f'{mo.capitalize()} is in the season: {seasons[map[mo]]}')
