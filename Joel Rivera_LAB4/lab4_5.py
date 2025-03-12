#lab4_5.py – Joel Rivera

#A: Print the last item in the given list
#myInfo = ['apple','banana','cherry']
#print(myInfo[3]), this index is out of range
myInfo = ['apple','banana','cherry']
print(myInfo[2])

#B: To make a valid copy, create a new list and copy the
#elements from the original list into the new list, rather
#than simply assigning the original list to a new variable,
#to ensure that the two lists are different
#myInfo = ['apple','banana','cherry']
#newInfo = myInfo, have to create a new list and store it in a variable

myInfo = ['apple','banana','cherry']
newInfo = list(myInfo)
print(f'{myInfo} \n{newInfo}')

#C: myInfo = 'sea'
#myInfo[0] = 'p' #Change the first letter from ‘s’ to ‘p’
#print(myInfo) #Print the value, cant change the index of a string, make the
#string a list, change the index and change back into a string
myInfo = 'sea'
newInfo=list(myInfo)
newInfo[0]='p'  
newString= ''.join(newInfo)
print(newString)  

#D: Print the items in reverse order, starting from the end of
#the list and ending at the beginning of the given list
#myInfo = [1, "two", 'three', 4]
#print(myInfo[-1:-4]), you cant use slicing to reverse the list, 
#you have to use the reverse method
myInfo = [1, "two", 'three', 4]
myInfo.reverse()
print(myInfo[:])

#E: Print the following as the example output based on the
#given list
#myInfo = [1, "two", 'three', 4]
#print(" ".join(myLst)), to get the expected output you need to use the join() andmap() methods to make the list one big string
#map() takes a function in the first parameter and passes the function to each iterable in the second paramter
 
myInfo = [1, "two", 'three', 4]
myInfo.insert(1,'<<<<')
myInfo.insert(3,'<<<<')
myInfo.insert(5,'<<<<')
newString=' '.join(map(str, myInfo))
print(newString)
