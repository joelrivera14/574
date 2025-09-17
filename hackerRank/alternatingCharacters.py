
a="AAAA"
b="BBBBB"
aB="ABABABAB"
Ba="BABABA"
aaaB="AAABBB"

def alternatingCharacters(s):
    # Write your code here
    sList = list(s)
    removeS= 0
    for i in range(len(sList)-1):
        if sList[i]==sList[i+1]:
            removeS +=1
    return removeS

print(alternatingCharacters(aaaB))