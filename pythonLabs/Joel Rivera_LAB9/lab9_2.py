#lab9_2.py – Joel Rivera

#define function nameFormat()
def nameFormat(first, middle, last):
    print(f'{first.title()} {middle[0].title()}. {last.title()}')

#define function main()
def main():
#calling nameFormat() with positional arguments
    nameFormat('john', 'stu', 'smith')
#calling nameFormat() with keyword arguments
    nameFormat(last = 'kennedy', first = 'john', middle = 'fitzgerald')

#calling main()
main()