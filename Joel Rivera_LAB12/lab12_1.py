#lab12_1.py – Joel Rivera

filename= 'USPres.txt'

def loop():
    with open(filename) as fi:
#enumerate() method is a built in python function that adds an index to an iterable
        for i,e in enumerate(fi):
            if i <3:
                print(e, end='')


def lst():
    with open(filename) as f:
#readlines() method returns a list of lines from the file
        newList= f.readlines()
#using slicing to interate only the first three items in the list
        for items in newList[:3]:
            print(items, end='')

loop()
print()
lst()