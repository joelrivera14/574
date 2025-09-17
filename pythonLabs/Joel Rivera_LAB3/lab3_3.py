#lab3_3.py - Joel Rivera

#prompt three integers
try: 
    one=int(input('Please enter the first integer: '))
    two=int(input('Please enter the second integer: '))
    three=int(input('Please enter the third integer: '))
    print('Before sorting:', one,two,three)
 #sorting the integers using the min(), max() functions
    h=max(one, two, three)
    s=min(one,two,three)
    m= one + two + three - h -  s 
 #printing all the numbers in order
    print('After sorting:', s,m,h)
except:
    print('Exceptions: Invalid input')

