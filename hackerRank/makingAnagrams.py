
a='cde'    
b='abc'

def makeAnagram(a, b):
    # Write your code here
    aList = list(a)
    bList = list(b)
    removeB = 0
    for same in bList:
        if same in aList:
            aList.remove(same)
        else:
            removeB +=1
    removeA = len(aList)
    return removeB + removeA

print(makeAnagram(a,b))