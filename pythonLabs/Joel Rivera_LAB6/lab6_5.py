#lab6_5.py – Joel Rivera

#A: n = eval(input("Enter a number: "))
#if n = 7:
#print("The square of", n,"=", n*2), == needs to be used for comparison
n = eval(input("Enter a number: "))
if n == 7:
    print("The square of", n,"=", n*2)

#B: n = 9
#if n > 5 and < 9:
#print("Yes")
#else:
#print("No"), the variable n needs to be added to the if statment
n = 9
if n > 5 and n < 9:
    print("Yes")
else:
    print("No")

#C: major = "Computer Science"
#if major == "Engineering Technology" Or "Computer Technology"
#print("CS in the Category"), the or needs to be in lower case, the colon 
#needed to be added at the end of the if statement and to execute the
#print function only when there is a match, the major variable needed to
#be compared to both strings
major = "Computer Science"
if major == "Engineering Technology" or major == "Computer Technology":
    print("CS in the Category")

#D: a, b = 1, 1.0
#if a = b:print("same"), == needs to be used for comparison
a, b = 1, 1.0
if a == b:print("same")