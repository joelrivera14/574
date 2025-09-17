#lab6_1.py – Joel Rivera

#prompting age
age = int(input('Please enter your age: '))

#if age < 0, invalid
if(age<0):
    print(f'invalid age')

#elif age < 2, baby
elif(age<=2):
    print(f"You're a baby")

#elif age > 2 age < 4, toddler
elif(age>=2 and age<4):
    print(f"You're a toddler")

#elif age > 4 age < 13, kid
elif(age>=4 and age<13):
    print(f"You're a kid")

#elif age > 13 age < 20, teenager
elif(age>=13 and age<20):
    print(f"You're a teenager")

#elif age > 20 age < 65, adult
elif(age>=20 and age<65):
    print(f"You're a adult")

#else 65+
else:
    print(f"You're a elder")