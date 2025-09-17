#lab9_1.py – Joel Rivera

#define function printList
def printList(p):
#printing each element 
    for e in p:
        print(f'{e}',  end=' ')
    print()

#define main() to create a list and call prinList()
def main():
    lst=['apple', 'banana', 'cherry']
#calling printList
    printList(lst)

#calling main()
main()