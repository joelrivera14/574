#lab11_2.py – Joel Rivera

#creating a dictionary 
rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}

#prompting input and printing the value of matching key
'''
try:
    year=int(input('Enter the # of years in the school <1-4>: '))
    if 1<=year<=4:
        print(f'Year {year} = {rank[year]}')
    else:
        print(f'Invalid years.')
except:
    print(f'Invalid input.')
'''
#trying a different way
try:
    year=int(input('Enter the # of years in the school <1-4>: '))
    print(f'Year {year} = {rank[year]}')
except (ValueError, KeyError):
    print(f'Invalid years.')