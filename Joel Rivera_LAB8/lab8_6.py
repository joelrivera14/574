#lab8_6.py – Joel Rivera
import random

#defining middle function with list paramter
def middle(lst):
    newlst = lst[:]
    if len(lst)<= 1:
        return newlst
    else:
        return newlst[1:-1]

#defining main function
def main():
#generating a random number
    n = random.randint(1,10)
#creating a list with n numbers
    numlist = list(range(1,n+1))
    if n == 1:
        print(f'No changes made to the list.')   
    print(f'List length = {n}\n{numlist}')
    print(middle(numlist))

#calling function
main()