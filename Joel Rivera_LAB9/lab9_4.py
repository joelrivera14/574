#lab9_4.py – Joel Rivera

#define printNames() with a parameter, '*' allows the function to accept
#any amount of arguments and collect them into tuple names
def printNames(*names):
    for e in names:
        print(f'{e}', end=' ')
    print()

printNames('Ann', 'Bianca', 'Coco', 'Dora', 'Emily')