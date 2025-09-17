#lab7_7.py - Joel Rivera

#implement a while loop to request numbers and append to a list
lst=[]
numbers =  eval(input('Enter a number or 0 to stop: '))
while numbers > 0 or numbers < 0:
    lst.append(numbers)
    numbers =  eval(input('Enter a number or 0 to stop: '))
#if 0 is entered, stop loop and dont append
    if numbers == 0:
        break
    
sum = sum(lst)
average = sum/len(lst)
print()
print(f'Sum = {sum:.2f}\nAverage = {average:.2f}\nNumber(s) entered:')
for e in lst:
    print(e, end=" ")
print()