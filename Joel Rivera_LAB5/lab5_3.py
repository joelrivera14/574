#lab5_3.py – Joel Rivera

#creating a list comprehension 
multiFour=[num*4 for num in range(11)]
print(f'{multiFour}')

#creating an empty list, and using a for loop to append each item
secList=[]
for num in multiFour:
    halved=int(num/2)
    secList.append(halved)
print(f'{secList}')

#using slicing to copy the list
thirdList=secList[:]
#using a for loop to iterate through the length of thirdList
for num in range(len(thirdList)):
    #replacing the original value with half value while in place
    thirdList[num] = int(thirdList[num]/2)
print(f'{thirdList}')