#lab9_3.py – Joel Rivera

#define nameFormat() with middle being optional
def nameFormat(first, last, middle=''):
    if middle:
#using f string to return a string instead of a tuple
        return f'{last.title()}, {first.title()} {middle[0].title()}.'
    else:
        return f'{last.title()}, {first.title()}'

#define main()
def main():
    print(nameFormat(last='bond', first='james'))
    print(nameFormat(last='jones', first='henry', middle='indiana'))

main()